// Green Guardian AI - Home Page Interactions
document.addEventListener('DOMContentLoaded', function() {
    
    // Animate elements on scroll
    function animateOnScroll() {
        const elements = document.querySelectorAll('.animate-on-scroll');
        const windowHeight = window.innerHeight;
        
        elements.forEach(element => {
            const elementTop = element.getBoundingClientRect().top;
            const elementVisible = 150;
            
            if (elementTop < windowHeight - elementVisible) {
                element.classList.add('animated');
            }
        });
    }
    
    // Initial check and add scroll listener
    animateOnScroll();
    window.addEventListener('scroll', animateOnScroll);
    
    // Add animate-on-scroll class to feature cards
    const featureCards = document.querySelectorAll('.feature-card');
    featureCards.forEach((card, index) => {
        card.classList.add('animate-on-scroll');
        card.style.animationDelay = `${index * 0.1}s`;
    });
    
    // Garden tip animation
    const tipOfDay = document.querySelector('.tip-of-day');
    if (tipOfDay) {
        tipOfDay.classList.add('animate-on-scroll');
    }
    
    // Parallax effect for floating elements
    window.addEventListener('scroll', function() {
        const scrolled = window.pageYOffset;
        const floatingElements = document.querySelectorAll('.floating-leaf');
        
        floatingElements.forEach((element, index) => {
            const speed = 0.2 + (index * 0.1);
            element.style.transform = `translateY(${scrolled * speed}px) rotate(${scrolled * 0.1}deg)`;
        });
    });
    
    // Interactive hover effects for feature cards
    featureCards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            const icon = this.querySelector('.feature-icon i');
            if (icon) {
                icon.style.animation = 'bounce 0.6s ease-in-out';
            }
        });
        
        card.addEventListener('mouseleave', function() {
            const icon = this.querySelector('.feature-icon i');
            if (icon) {
                icon.style.animation = '';
            }
        });
    });
    
    // Hero CTA button ripple effect
    const ctaButton = document.querySelector('.hero-cta');
    if (ctaButton) {
        ctaButton.addEventListener('click', function(e) {
            const ripple = document.createElement('span');
            const rect = this.getBoundingClientRect();
            const size = Math.max(rect.width, rect.height);
            const x = e.clientX - rect.left - size / 2;
            const y = e.clientY - rect.top - size / 2;
            
            ripple.style.width = ripple.style.height = size + 'px';
            ripple.style.left = x + 'px';
            ripple.style.top = y + 'px';
            ripple.classList.add('ripple');
            
            this.appendChild(ripple);
            
            setTimeout(() => {
                ripple.remove();
            }, 600);
        });
    }
    
    // Dynamic garden tip rotation
    const gardenTips = [
        "🌱 Water your plants early in the morning to reduce evaporation and prevent fungal diseases. Your plants will thank you!",
        "🌿 Companion planting helps deter pests naturally. Try planting marigolds near tomatoes!",
        "🌻 Rotate your crops each season to maintain soil health and prevent disease buildup.",
        "🦋 Create a pollinator-friendly garden by planting native flowers and avoiding pesticides.",
        "🌰 Compost your kitchen scraps to create nutrient-rich soil for your garden.",
        "🌸 Mulching around plants helps retain moisture and suppress weeds naturally.",
        "🐝 Plant flowers that bloom at different times to support pollinators throughout the season."
    ];
    
    let currentTip = 0;
    const tipContent = document.querySelector('.tip-content p');
    
    function rotateTip() {
        if (tipContent) {
            tipContent.style.opacity = '0';
            setTimeout(() => {
                currentTip = (currentTip + 1) % gardenTips.length;
                tipContent.textContent = gardenTips[currentTip];
                tipContent.style.opacity = '1';
            }, 300);
        }
    }
    
    // Rotate tips every 10 seconds
    setInterval(rotateTip, 10000);
    
    // Add floating particles effect
    function createFloatingParticle() {
        const particles = ['🌿', '🍃', '✨', '🌸', '🦋'];
        const particle = document.createElement('div');
        particle.textContent = particles[Math.floor(Math.random() * particles.length)];
        particle.style.cssText = `
            position: fixed;
            left: ${Math.random() * 100}vw;
            top: 100vh;
            font-size: 1rem;
            pointer-events: none;
            z-index: 1;
            opacity: 0.7;
            animation: floatUpAndFade 8s linear forwards;
        `;
        
        document.body.appendChild(particle);
        
        setTimeout(() => {
            if (particle.parentNode) {
                particle.parentNode.removeChild(particle);
            }
        }, 8000);
    }
    
    // Create floating particles periodically
    setInterval(createFloatingParticle, 3000);
    
    // Smooth scroll for navigation links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
    
    // Add typewriter effect to hero title
    function typewriterEffect(element, text, speed = 100) {
        element.innerHTML = '';
        let i = 0;
        
        function typeChar() {
            if (i < text.length) {
                element.innerHTML += text.charAt(i);
                i++;
                setTimeout(typeChar, speed);
            }
        }
        
        typeChar();
    }
    
    // Apply typewriter effect to hero title after a delay
    const heroTitle = document.querySelector('.hero-title');
    if (heroTitle) {
        const originalText = heroTitle.textContent;
        setTimeout(() => {
            typewriterEffect(heroTitle, originalText, 80);
        }, 500);
    }
    
    // Weather integration (placeholder for future implementation)
    function loadGardenWeather() {
        // This would integrate with a weather API
        console.log('Garden weather widget ready for integration');
    }
    
    // Initialize weather widget
    loadGardenWeather();
    
    // Add sparkle effect on feature card hover
    function createSparkles(element) {
        const rect = element.getBoundingClientRect();
        const sparkleContainer = document.createElement('div');
        sparkleContainer.style.cssText = `
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            pointer-events: none;
            z-index: 10;
        `;
        
        for (let i = 0; i < 6; i++) {
            const sparkle = document.createElement('div');
            sparkle.textContent = '✨';
            sparkle.style.cssText = `
                position: absolute;
                left: ${Math.random() * 100}%;
                top: ${Math.random() * 100}%;
                font-size: 0.8rem;
                animation: sparkle 1.5s ease-out forwards;
                opacity: 0;
            `;
            sparkleContainer.appendChild(sparkle);
        }
        
        element.appendChild(sparkleContainer);
        
        setTimeout(() => {
            if (sparkleContainer.parentNode) {
                sparkleContainer.parentNode.removeChild(sparkleContainer);
            }
        }, 1500);
    }
    
    // Add sparkle effect to feature cards on hover
    featureCards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            createSparkles(this);
        });
    });
});

// Add CSS animations through JavaScript
const style = document.createElement('style');
style.textContent = `
    @keyframes floatUpAndFade {
        0% {
            transform: translateY(0) rotate(0deg);
            opacity: 0.7;
        }
        50% {
            opacity: 1;
        }
        100% {
            transform: translateY(-100vh) rotate(360deg);
            opacity: 0;
        }
    }
    
    @keyframes sparkle {
        0% {
            transform: scale(0) rotate(0deg);
            opacity: 1;
        }
        50% {
            transform: scale(1) rotate(180deg);
            opacity: 1;
        }
        100% {
            transform: scale(0) rotate(360deg);
            opacity: 0;
        }
    }
    
    .ripple {
        position: absolute;
        border-radius: 50%;
        background: rgba(255, 255, 255, 0.4);
        animation: ripple-animation 0.6s linear;
        pointer-events: none;
    }
    
    @keyframes ripple-animation {
        0% {
            transform: scale(0);
            opacity: 1;
        }
        100% {
            transform: scale(4);
            opacity: 0;
        }
    }
    
    .tip-content p {
        transition: opacity 0.3s ease;
    }
`;
document.head.appendChild(style);
