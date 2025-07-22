// Garden Theme JavaScript for Enhanced Interactivity
document.addEventListener('DOMContentLoaded', function() {
    
    // Logo/Form Animation on Page Load
    const formElements = document.querySelectorAll('.text-center h1, form.user .form-group, .btn-user');
    formElements.forEach((element, index) => {
        element.style.animationDelay = `${index * 0.1}s`;
    });

    // Enhanced animations for register form
    const isRegisterPage = document.querySelector('input[name="first_name"]');
    if (isRegisterPage) {
        // Add special register page animations
        const formRows = document.querySelectorAll('.form-group.row, .form-group');
        formRows.forEach((row, index) => {
            row.style.animationDelay = `${(index + 2) * 0.15}s`;
        });
        
        // Add garden growing animation to submit button
        const submitBtn = document.querySelector('.btn-user');
        if (submitBtn) {
            submitBtn.addEventListener('mouseenter', function() {
                this.innerHTML = '🌱 Watch Your Garden Grow! 🌱';
            });
            
            submitBtn.addEventListener('mouseleave', function() {
                this.innerHTML = '🌱 Plant Your Account';
            });
        }
    }

    // Enhanced Input Focus Effects
    const inputs = document.querySelectorAll('.form-control-user');
    inputs.forEach(input => {
        // Add focus event listeners
        input.addEventListener('focus', function() {
            this.parentElement.classList.add('focused');
            createSparkles(this);
        });

        input.addEventListener('blur', function() {
            if (!this.value) {
                this.parentElement.classList.remove('focused');
            }
        });

        // Add typing effect
        input.addEventListener('input', function() {
            if (this.value) {
                this.parentElement.classList.add('has-value');
            } else {
                this.parentElement.classList.remove('has-value');
            }
        });
    });

    // Create sparkle effect on input focus
    function createSparkles(element) {
        const rect = element.getBoundingClientRect();
        const sparklesContainer = document.createElement('div');
        sparklesContainer.className = 'sparkles';
        sparklesContainer.style.position = 'absolute';
        sparklesContainer.style.top = rect.top + 'px';
        sparklesContainer.style.left = rect.left + 'px';
        sparklesContainer.style.width = rect.width + 'px';
        sparklesContainer.style.height = rect.height + 'px';
        sparklesContainer.style.pointerEvents = 'none';
        sparklesContainer.style.zIndex = '1000';

        for (let i = 0; i < 5; i++) {
            const sparkle = document.createElement('div');
            sparkle.style.position = 'absolute';
            sparkle.style.width = '4px';
            sparkle.style.height = '4px';
            sparkle.style.background = '#A3D9A5';
            sparkle.style.borderRadius = '50%';
            sparkle.style.left = Math.random() * rect.width + 'px';
            sparkle.style.top = Math.random() * rect.height + 'px';
            sparkle.style.animation = 'sparkle 1s ease-out forwards';
            sparklesContainer.appendChild(sparkle);
        }

        document.body.appendChild(sparklesContainer);

        setTimeout(() => {
            document.body.removeChild(sparklesContainer);
        }, 1000);
    }

    // Enhanced Button Interactions
    const submitButton = document.querySelector('.btn-user');
    if (submitButton) {
        submitButton.addEventListener('click', function(e) {
            // Add ripple effect
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

    // Remember Me Checkbox Enhancement
    const checkbox = document.querySelector('#customCheck');
    if (checkbox) {
        checkbox.addEventListener('change', function() {
            if (this.checked) {
                // Add extra sprouting animation
                const label = this.nextElementSibling;
                label.style.transform = 'scale(1.05)';
                setTimeout(() => {
                    label.style.transform = 'scale(1)';
                }, 300);
            }
        });
    }

    // Parallax effect for background elements
    window.addEventListener('scroll', function() {
        const scrolled = window.pageYOffset;
        const parallaxElements = document.querySelectorAll('.floating-leaves');
        parallaxElements.forEach(element => {
            element.style.transform = `translateY(${scrolled * 0.5}px)`;
        });
    });

    // Mouse movement parallax for card
    const card = document.querySelector('.card');
    if (card) {
        document.addEventListener('mousemove', function(e) {
            const xAxis = (window.innerWidth / 2 - e.pageX) / 25;
            const yAxis = (window.innerHeight / 2 - e.pageY) / 25;
            card.style.transform = `rotateY(${xAxis}deg) rotateX(${yAxis}deg)`;
        });

        document.addEventListener('mouseleave', function() {
            card.style.transform = 'rotateY(0deg) rotateX(0deg)';
        });
    }

    // Add random floating elements periodically
    function createFloatingElement() {
        const elements = ['🌿', '🍃', '🌱', '🌸', '🦋'];
        const element = document.createElement('div');
        element.textContent = elements[Math.floor(Math.random() * elements.length)];
        element.style.position = 'fixed';
        element.style.left = Math.random() * 100 + 'vw';
        element.style.top = '100vh';
        element.style.fontSize = '1.5rem';
        element.style.pointerEvents = 'none';
        element.style.zIndex = '1';
        element.style.animation = `floatUp ${5 + Math.random() * 5}s linear forwards`;
        
        document.body.appendChild(element);
        
        setTimeout(() => {
            if (element.parentNode) {
                element.parentNode.removeChild(element);
            }
        }, 10000);
    }

    // Create floating elements periodically
    setInterval(createFloatingElement, 3000);

    // Enhanced alert dismissal
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(alert => {
        const closeButton = alert.querySelector('.close');
        if (closeButton) {
            closeButton.addEventListener('click', function() {
                alert.style.animation = 'slideOutUp 0.5s ease-in forwards';
                setTimeout(() => {
                    alert.remove();
                }, 500);
            });
        }
    });

    // Form validation with garden-themed feedback
    const form = document.querySelector('form.user');
    if (form) {
        form.addEventListener('submit', function(e) {
            const emailInput = this.querySelector('input[type="email"]');
            const passwordInput = this.querySelector('input[type="password"]');
            const repeatPasswordInput = this.querySelector('input[name="repeat_password"]');
            
            // Check if it's register form
            const isRegisterForm = this.querySelector('input[name="first_name"]');
            
            if (isRegisterForm) {
                // Register form validation
                const firstNameInput = this.querySelector('input[name="first_name"]');
                const lastNameInput = this.querySelector('input[name="last_name"]');
                const phoneInput = this.querySelector('input[name="phone_number"]');
                
                if (!firstNameInput.value || !lastNameInput.value || !phoneInput.value || !emailInput.value || !passwordInput.value || !repeatPasswordInput.value) {
                    e.preventDefault();
                    showGardenNotification('Please fill in all fields to plant your garden account! 🌱');
                    return;
                }
                
                if (passwordInput.value !== repeatPasswordInput.value) {
                    e.preventDefault();
                    showGardenNotification('Passwords don\'t match! Make sure they bloom together 🌸');
                    return;
                }
                
                if (passwordInput.value.length < 6) {
                    e.preventDefault();
                    showGardenNotification('Password should be at least 6 characters to grow strong! 🌳');
                    return;
                }
                
                // Add loading animation to button
                submitButton.innerHTML = '<span class="loading-dots">Planting your garden</span><span class="dots">...</span>';
                submitButton.disabled = true;
            } else {
                // Login form validation
                if (!emailInput.value || !passwordInput.value) {
                    e.preventDefault();
                    showGardenNotification('Please fill in all fields to let your login bloom! 🌱');
                    return;
                }
                
                // Add loading animation to button
                submitButton.innerHTML = '<span class="loading-dots">Planting seeds</span><span class="dots">...</span>';
                submitButton.disabled = true;
            }
        });
        
        // Real-time password confirmation validation for register form
        const passwordInput = form.querySelector('input[name="password"]');
        const repeatPasswordInput = form.querySelector('input[name="repeat_password"]');
        
        if (passwordInput && repeatPasswordInput) {
            function validatePasswordMatch() {
                if (repeatPasswordInput.value && passwordInput.value !== repeatPasswordInput.value) {
                    repeatPasswordInput.setCustomValidity('Passwords do not match');
                    repeatPasswordInput.style.borderColor = '#ff6b6b';
                } else {
                    repeatPasswordInput.setCustomValidity('');
                    if (repeatPasswordInput.value) {
                        repeatPasswordInput.style.borderColor = 'var(--garden-secondary)';
                    }
                }
            }
            
            passwordInput.addEventListener('input', validatePasswordMatch);
            repeatPasswordInput.addEventListener('input', validatePasswordMatch);
        }
    }

    function showGardenNotification(message) {
        const notification = document.createElement('div');
        notification.className = 'garden-notification';
        notification.innerHTML = `
            <div class="notification-content">
                🌿 ${message}
            </div>
        `;
        notification.style.cssText = `
            position: fixed;
            top: 20px;
            right: 20px;
            background: linear-gradient(135deg, #A3D9A5, #3A7D44);
            color: white;
            padding: 15px 25px;
            border-radius: 25px;
            box-shadow: 0 10px 25px rgba(58, 125, 68, 0.3);
            z-index: 9999;
            animation: slideInRight 0.5s ease-out;
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.3);
        `;
        
        document.body.appendChild(notification);
        
        setTimeout(() => {
            notification.style.animation = 'slideOutRight 0.5s ease-in forwards';
            setTimeout(() => {
                if (notification.parentNode) {
                    notification.parentNode.removeChild(notification);
                }
            }, 500);
        }, 3000);
    }
});

// Add dynamic CSS animations
const style = document.createElement('style');
style.textContent = `
    @keyframes sparkle {
        0% { transform: scale(0) rotate(0deg); opacity: 1; }
        50% { transform: scale(1) rotate(180deg); opacity: 0.8; }
        100% { transform: scale(0) rotate(360deg); opacity: 0; }
    }
    
    @keyframes ripple {
        0% { transform: scale(0); opacity: 1; }
        100% { transform: scale(4); opacity: 0; }
    }
    
    .ripple {
        position: absolute;
        border-radius: 50%;
        background: rgba(255, 255, 255, 0.4);
        animation: ripple 0.6s linear;
        pointer-events: none;
    }
    
    @keyframes floatUp {
        0% { transform: translateY(0) rotate(0deg); opacity: 0; }
        10% { opacity: 0.8; }
        90% { opacity: 0.8; }
        100% { transform: translateY(-100vh) rotate(360deg); opacity: 0; }
    }
    
    @keyframes slideInRight {
        from { transform: translateX(100%); opacity: 0; }
        to { transform: translateX(0); opacity: 1; }
    }
    
    @keyframes slideOutRight {
        from { transform: translateX(0); opacity: 1; }
        to { transform: translateX(100%); opacity: 0; }
    }
    
    @keyframes slideOutUp {
        from { transform: translateY(0); opacity: 1; }
        to { transform: translateY(-100%); opacity: 0; }
    }
    
    .loading-dots {
        animation: loadingPulse 1.5s ease-in-out infinite;
    }
    
    @keyframes loadingPulse {
        0%, 100% { opacity: 1; }
        50% { opacity: 0.5; }
    }
    
    .dots {
        animation: dotFlashing 1.4s infinite linear;
    }
    
    @keyframes dotFlashing {
        0% { content: ''; }
        25% { content: '.'; }
        50% { content: '..'; }
        75% { content: '...'; }
        100% { content: ''; }
    }
    
    .focused .form-control-user {
        transform: scale(1.02);
    }
    
    .has-value .form-control-user {
        background: rgba(163, 217, 165, 0.1) !important;
    }
`;
document.head.appendChild(style);
