document.addEventListener('DOMContentLoaded', function() {
    
    // ==========================================================================
    // 1. LOADER ANIMATION HIDING
    // ==========================================================================
    const loader = document.getElementById('loader');
    if (loader) {
        window.addEventListener('load', function() {
            setTimeout(function() {
                loader.style.opacity = '0';
                loader.style.visibility = 'hidden';
            }, 300);
        });
        // Fallback in case load event already fired
        if (document.readyState === 'complete') {
            setTimeout(function() {
                loader.style.opacity = '0';
                loader.style.visibility = 'hidden';
            }, 300);
        }
    }

    // ==========================================================================
    // 2. THEME SWITCHING (LIGHT / DARK MODE)
    // ==========================================================================
    const themeToggle = document.getElementById('themeToggle');
    const htmlElement = document.documentElement;
    
    // Check saved theme or system preference
    const savedTheme = localStorage.getItem('theme');
    const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
    
    if (savedTheme) {
        htmlElement.setAttribute('data-theme', savedTheme);
        updateThemeToggleIcon(savedTheme);
    } else if (prefersDark) {
        htmlElement.setAttribute('data-theme', 'dark');
        updateThemeToggleIcon('dark');
    }

    themeToggle.addEventListener('click', function() {
        const currentTheme = htmlElement.getAttribute('data-theme');
        const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
        
        htmlElement.setAttribute('data-theme', newTheme);
        localStorage.setItem('theme', newTheme);
        updateThemeToggleIcon(newTheme);
    });

    function updateThemeToggleIcon(theme) {
        const icon = themeToggle.querySelector('i');
        if (theme === 'dark') {
            icon.className = 'fa-solid fa-sun';
        } else {
            icon.className = 'fa-solid fa-moon';
        }
    }

    // ==========================================================================
    // 3. STICKY NAVBAR & BACK-TO-TOP TRIGGER ON SCROLL
    // ==========================================================================
    const navbar = document.getElementById('mainNavbar');
    const scrollToTopBtn = document.getElementById('scrollToTop');

    window.addEventListener('scroll', function() {
        if (window.scrollY > 50) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }

        if (window.scrollY > 400) {
            scrollToTopBtn.classList.add('visible');
        } else {
            scrollToTopBtn.classList.remove('visible');
        }
    });

    // Scroll to Top click
    scrollToTopBtn.addEventListener('click', function() {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    });

    // ==========================================================================
    // 4. SCROLLSPY (ACTIVE LINK ON SCROLL)
    // ==========================================================================
    const sections = document.querySelectorAll('section, header');
    const navLinks = document.querySelectorAll('.navbar-nav .nav-link');

    window.addEventListener('scroll', function() {
        let currentSectionId = '';
        
        sections.forEach(section => {
            const sectionTop = section.offsetTop - 150; // offset for fixed nav
            const sectionHeight = section.clientHeight;
            if (window.scrollY >= sectionTop && window.scrollY < sectionTop + sectionHeight) {
                currentSectionId = section.getAttribute('id');
            }
        });

        navLinks.forEach(link => {
            link.classList.remove('active');
            if (link.getAttribute('href') === `#${currentSectionId}`) {
                link.classList.add('active');
            }
        });
    });

    // ==========================================================================
    // 5. ANIMATED TYPING EFFECT (TYPED.JS)
    // ==========================================================================
    const typedTarget = document.getElementById('typed-roles');
    if (typedTarget) {
        const rolesString = typedTarget.getAttribute('data-roles');
        // Fallback roles if data-roles is missing or empty
        const rolesArray = rolesString 
            ? rolesString.split(',').map(role => role.trim()) 
            : ["Computer Science Student", "AI Enthusiast", "Backend Developer", "Problem Solver"];
            
        new Typed('#typed-roles', {
            strings: rolesArray,
            typeSpeed: 60,
            backSpeed: 45,
            backDelay: 2000,
            startDelay: 500,
            loop: true,
            showCursor: true,
            cursorChar: '|'
        });
    }

    // ==========================================================================
    // 6. DYNAMIC PROJECTS FILTERING ANIMATION
    // ==========================================================================
    const filterButtons = document.querySelectorAll('.filter-btn');
    const projectItems = document.querySelectorAll('.project-item-col');

    filterButtons.forEach(button => {
        button.addEventListener('click', function() {
            // Remove active from all buttons
            filterButtons.forEach(btn => btn.classList.remove('active'));
            this.classList.add('active');

            const filterValue = this.getAttribute('data-filter').toLowerCase();

            projectItems.forEach(item => {
                const itemTechs = item.getAttribute('data-technologies').toLowerCase();
                
                if (filterValue === 'all') {
                    // Reset styling
                    item.style.display = 'block';
                    setTimeout(() => {
                        item.style.opacity = '1';
                        item.style.transform = 'scale(1)';
                    }, 50);
                } else if (itemTechs.includes(filterValue)) {
                    item.style.display = 'block';
                    setTimeout(() => {
                        item.style.opacity = '1';
                        item.style.transform = 'scale(1)';
                    }, 50);
                } else {
                    item.style.opacity = '0';
                    item.style.transform = 'scale(0.8)';
                    setTimeout(() => {
                        item.style.display = 'none';
                    }, 400); // match transition duration
                }
            });
        });
    });

    // ==========================================================================
    // 7. CONTACT FORM SUBMISSION WITH AJAX & VALIDATION
    // ==========================================================================
    const contactForm = document.getElementById('contactForm');
    if (contactForm) {
        $(contactForm).on('submit', function(e) {
            e.preventDefault();
            
            const form = $(this);
            const submitBtn = form.find('button[type="submit"]');
            const spinner = form.find('.contact-spinner');
            const btnText = form.find('.btn-text');
            const successAlert = $('#contactSuccessAlert');
            const errorAlert = $('#contactErrorAlert');

            // Hide previous alerts
            successAlert.hide();
            errorAlert.hide();

            // Client-side validations
            const name = $('#fullName').val().trim();
            const email = $('#emailAddress').val().trim();
            const subject = $('#subject').val().trim();
            const message = $('#message').val().trim();

            if (!name || !email || !subject || !message) {
                errorAlert.text('Please fill in all required fields.').fadeIn();
                return;
            }

            // Disable button and show loader
            submitBtn.prop('disabled', true);
            spinner.show();
            btnText.text('Sending...');

            $.ajax({
                url: form.attr('action'),
                type: 'POST',
                data: form.serialize(),
                headers: {
                    'X-Requested-With': 'XMLHttpRequest'
                },
                success: function(response) {
                    submitBtn.prop('disabled', false);
                    spinner.hide();
                    btnText.text('Send Message');
                    
                    if (response.status === 'success') {
                        successAlert.text(response.message).fadeIn();
                        form[0].reset();
                    } else {
                        errorAlert.text(response.message).fadeIn();
                    }
                },
                error: function(xhr) {
                    submitBtn.prop('disabled', false);
                    spinner.hide();
                    btnText.text('Send Message');
                    
                    let errorMsg = 'An error occurred while sending your message. Please check your connection and try again.';
                    if (xhr.responseJSON && xhr.responseJSON.message) {
                        errorMsg = xhr.responseJSON.message;
                    }
                    errorAlert.text(errorMsg).fadeIn();
                }
            });
        });
    }

});
