// Temporizador de mensagens do sistema

setTimeout(() => {
        const messages = document.querySelectorAll('.message');
        messages.forEach((msg) => {
            msg.classList.add('opacity-0', 'transition-opacity', 'duration-1000');
            setTimeout(() => msg.remove(), 1000);
        });
    }, 4000);