const the_animation = document.querySelectorAll('.animationY');
const the_animation2 = document.querySelectorAll('.animationL');
const the_animation3 = document.querySelectorAll('.animationR');
const the_animation4 = document.querySelectorAll('.animationD');
const the_animation5 = document.querySelectorAll('.animationS');

const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
        if (entry.isIntersecting) {
            entry.target.classList.add('scroll-animationY')
        }
        else {
            entry.target.classList.remove('scroll-animationY')
        }

    })
},
    {
        threshold: 0.5
    });

const observer2 = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
        if (entry.isIntersecting) {
            entry.target.classList.add('scroll-animationL')
        }
        else {
            entry.target.classList.remove('scroll-animationL')
        }

    })
},
    {
        threshold: 0.5
    });

const observer3 = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
        if (entry.isIntersecting) {
            entry.target.classList.add('scroll-animationR')
        }
        else {
            entry.target.classList.remove('scroll-animationR')
        }

    })
},
    {
        threshold: 0.5
    });

const observer4 = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
        if (entry.isIntersecting) {
            entry.target.classList.add('scroll-animationD')
        }
        else {
            entry.target.classList.remove('scroll-animationD')
        }

    })
},
    {
        threshold: 0.5
    });

const observer5 = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
        if (entry.isIntersecting) {
            entry.target.classList.add('scroll-animationS')
        }
        else {
            entry.target.classList.remove('scroll-animationS')
        }

    })
},
    {
        threshold: 0.5
    });


//
for (let i = 0; i < the_animation.length; i++) {
    const elements = the_animation[i];

    observer.observe(elements);
}

//
for (let i = 0; i < the_animation2.length; i++) {
    const elements = the_animation2[i];

    observer2.observe(elements);
}

//

for (let i = 0; i < the_animation3.length; i++) {
    const elements = the_animation3[i];

    observer3.observe(elements);
}

//

for (let i = 0; i < the_animation4.length; i++) {
    const elements = the_animation4[i];

    observer4.observe(elements);
}

//

for (let i = 0; i < the_animation5.length; i++) {
    const elements = the_animation5[i];

    observer5.observe(elements);
}