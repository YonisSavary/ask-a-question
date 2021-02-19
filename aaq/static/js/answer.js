
let to_origin_button = document.querySelector("#to_origin_button");
let parent_id = document.querySelector("#id_parent");

if (to_origin_button !== null)
{
    to_origin_button.style.visibility = "hidden"
    to_origin_button.addEventListener("click", ()=>{
        to_origin_button.style.visibility = "hidden"
        document.querySelector("#form_sample").innerText = "";
        document.querySelector("#form_title").innerText = "Poster un commentaire";
        parent_id.value = "";
    })
}

function addComment(evt){
    document.querySelector("#comment_form_section").scrollIntoView()
    to_origin_button.style.visibility = "visible";
    evt.preventDefault();
    let tar = evt.target.id;
    tar = tar.replace(/.{0,}_/, "");

    let content = document.querySelector("#comment_content_"+tar).innerText;
    let name = document.querySelector("#comment_name_"+tar).innerText;

    document.querySelector("#form_title").innerText = "Répondre à " + name;
    document.querySelector("#form_sample").innerText = content;
    parent_id.value = tar;
}

document.querySelectorAll(".comment_button").forEach(elem=>{
    elem.addEventListener("click", addComment)
})

document.querySelectorAll(".comment_section").forEach(elem=>{
    if (!elem.hasAttribute("target")) return 0;
    let targetId = elem.getAttribute("target")
    let target = document.querySelector(targetId);
    elem.classList.remove("card")
    elem.classList.add("comment-response")
    target.appendChild(elem);
})