from langchain.prompts import PromptTemplate
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.summarize import load_summarize_chain
from langchain.document_loaders import YoutubeLoader, WebBaseLoader
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.callbacks.base import BaseCallbackManager
from langchain.llms import OpenAI
import queue
import threading
import os
from dotenv import load_dotenv

load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

class ThreadedGenerator:
    def __init__(self):
        self.queue = queue.Queue()

    def __iter__(self):
        return self

    def __next__(self):
        item = self.queue.get()
        if item is StopIteration:
            raise item
        return item

    def send(self, data):
        self.queue.put(data)

    def close(self):
        self.queue.put(StopIteration)


class ChainStreamHandler(StreamingStdOutCallbackHandler):
    def __init__(self, gen):
        super().__init__()
        self.gen = gen

    def on_llm_new_token(self, token: str, **kwargs):
        self.gen.send(token)


def llm_thread(g, url, article):
    try:
        llm = OpenAI(
            verbose=True,
            streaming=True,
            callback_manager=BaseCallbackManager([ChainStreamHandler(g)]),
            temperature=0.7,
        )
        # llm(prompt)
        prompt_template = """Write a concise summary of the following extracting the key information:

        {text}

        CONCISE SUMMARY:"""

        PROMPT = PromptTemplate(
            input_variables=["text"],
            template=prompt_template
        )

        refine_template = """
            Your job is to produce a final summary\
            We have provided an existing summary up to a certain point : {existing_answer}\n
            We have the opportunity to refine the existing summary"
            (only if needed) with some more context below.\n"
            -------------\n
            {text}\n
            -------------\n
            Given the new context, refine the original summary
            If the context isn't useful, return the original summary.
        """

        REFINE_PROMPT = PromptTemplate(
            input_variables=["existing_answer", "text"],
            template=refine_template,
        )

        if article:
            loader = WebBaseLoader(url)
        else:
            loader = YoutubeLoader.from_youtube_url(url)

        docs = loader.load()

        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=2000,
            chunk_overlap=100,
        )
        splitted_docs = text_splitter.split_documents(docs)
        chain = load_summarize_chain(llm, chain_type="refine",
                                     question_prompt=PROMPT,
                                     refine_prompt=REFINE_PROMPT)

        chain({"input_documents": splitted_docs}, return_only_outputs=True)
        # chain.run(splitted_docs)
    finally:
        g.close()


def chain(url, article = False):
    g = ThreadedGenerator()
    threading.Thread(target=llm_thread, args=(g, url, article)).start()
    return g



if __name__ == '__main__':
    app.run(threaded=True, debug=True)
