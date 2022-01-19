var coll = document.getElementsByClassName("collapsible");
var i;

for (i = 0; i < coll.length; i++) {
  coll[i].addEventListener("click", function() {
    this.classList.toggle("active");
    var about = this.nextElementSibling;
    if (about.style.display === "block") {
      about.style.display = "none";
    } else {
      about.style.display = "block";
    }
  });
}
