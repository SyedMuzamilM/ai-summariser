(async () => {
  const body = document.querySelector("body");

  if (window.location.href.includes("youtube.com")) {
    if (window.location.href.includes("watch")) {
      console.log("youtube");
      const buttonsElement = document.getElementById(
        "top-level-buttons-computed"
      );
      const element = createYTButton();
      element.addEventListener("click", (e) => {
        e.preventDefault();
        console.log(window.location.href);
      });
      buttonsElement.appendChild(element);
    }
  } else {
    const element = createElement();
    element.addEventListener("click", (e) => {
      e.preventDefault();
      console.log(window.location.href);
    });
    body.appendChild(element);
  }
})();

function createElement() {
  const container = document.createElement("div");
  container.style.position = "fixed";
  container.style.right = "-3.5%";
  container.style.top = "50%";
  container.style.rotate = "-90deg";
  container.style.transform = "translateY(-50%)";

  const button = document.createElement("button");
  button.textContent = "Summarize";
  button.style.backgroundColor = "red";
  button.style.borderTopRightRadius = "16px";
  button.style.borderTopLeftRadius = "16px";
  button.style.color = "white";
  button.style.padding = "0.25rem 1rem";
  button.style.border = "none";
  button.style.cursor = "pointer";

  container.appendChild(button);

  return container;
}

function createYTButton() {
  const button = document.createElement("button");
  button.textContent = "Summarize";
  button.style.backgroundColor = "red";
  button.style.borderRadius = "18px";
  button.style.height = "36px";
  button.style.fontSize = "14px";
  button.style.color = "white";
  button.style.padding = "0 16px";
  button.style.border = "none";
  button.style.cursor = "pointer";
}
