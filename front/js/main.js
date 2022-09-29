window.addEventListener("scroll", (event)=> {
    let scrollY = this.scrollY;
    console.log(scrollY);
    if (scrollY >= 1000) {
        document.querySelectorAll(".scroll-induce")[0].classList.remove("visible");
    }
    
})