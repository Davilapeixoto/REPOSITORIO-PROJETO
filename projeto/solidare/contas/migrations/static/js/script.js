// ROLAGEM SUAVE PARA ÂNCORAS
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const destino = document.querySelector(this.getAttribute('href'));
        if (destino) {
            destino.scrollIntoView({
                behavior: 'smooth'
            });
        }
    });
});

// BOTÃO VOLTAR AO TOPO
const botaoTopo = document.createElement('button');
botaoTopo.innerText = "↑ Topo";
botaoTopo.style.position = "fixed";
botaoTopo.style.bottom = "20px";
botaoTopo.style.right = "20px";
botaoTopo.style.padding = "10px 15px";
botaoTopo.style.background = "#000";
botaoTopo.style.color = "#fff";
botaoTopo.style.border = "none";
botaoTopo.style.borderRadius = "8px";
botaoTopo.style.cursor = "pointer";
botaoTopo.style.display = "none";
document.body.appendChild(botaoTopo);

window.addEventListener('scroll', () => {
    if (window.scrollY > 200) {
        botaoTopo.style.display = 'block';
    } else {
        botaoTopo.style.display = 'none';
    }
});

botaoTopo.addEventListener('click', () => {
    window.scrollTo({
        top: 0,
        behavior: 'smooth'
    });
});
