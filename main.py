import argparse

from ai.summariser import youtube_video_summariser, article_summariser

def main(args):
    if args.url:
        url = args.url
    else:
        url = input("Please enter a URL: ")
    
    if args.article:
        summary = article_summariser(url)
    elif args.video:
        summary = youtube_video_summariser(url)
    else:
        print('Provide the arguments -a for article or -v for video')
        return
    

    file_name = "article_summary.md" if args.article else "video_summary.md"

    with open(file_name, 'w') as file:
        file.write(summary)
        
    file.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Fetch YouTube video information and generate a markdown block"
    )
    parser.add_argument("-u", "--url", help="YouTube video URL")
    parser.add_argument(
        "-a", "--article", action="store_true", help="Summarize the article"
    )
    parser.add_argument(
        "-v", "--video", action="store_true", help="Summarize the video"
    )
    args = parser.parse_args()
    main(args)
