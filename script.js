document.querySelector('.collapse-btn').addEventListener('click', () => {
    document.querySelector('.left-menu').classList.toggle('collapsed');
});

function resizePage() {
    const width = window.innerWidth;
    let scale = 10;

    if (width >= 992 && width <= 1600) {
        scale = 0.9;
    } else if (width >= 700 && width <= 767) {
        scale = 0.8;
    } else if (width >= 600 && width < 700) {
        scale = 0.75;
    } else if (width <= 600) {
        scale = 0.5;
    }

    document.body.style.transform = `scale(${scale})`;
}

window.addEventListener('resize', resizePage);
resizePage();
