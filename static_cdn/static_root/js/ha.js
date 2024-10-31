function showCourses() {
	var x = document.getElementById("dropdown-arrow").name;
	//alert(x);

	if (x == 1) {
		// Change the icon
		document.getElementById("dropdown-arrow").src = '';

		// Show the Menu
		document.getElementById("course-link-div").style.display = 'block';

		// Change the color of link
		//document.getElementById("courses-li").style.background = '#fff';

		// Change the value
		document.getElementById("dropdown-arrow").name = 2;

	} else {
		// Means to close the button
		// Change the icon
		document.getElementById("dropdown-arrow").src = 'icons/arrow_right.svg';

		// Show the Menu
		document.getElementById("course-link-div").style.display = 'none';

		// Change the color of link
		//document.getElementById("courses-li").style.background = '#fff';

		// Change the value
		document.getElementById("dropdown-arrow").name = 1;

	}

	//alert(x);
}

function showCourses2() {
	var x = document.getElementById("dropdown-arrow").name;
	//alert(x);

	if (x == 1) {
		// Change the icon
		document.getElementById("dropdown-arrow").src = '../icons/arrow_down_menu.svg';

		// Show the Menu
		document.getElementById("course-link-div").style.display = 'block';

		// Change the color of link
		//document.getElementById("courses-li").style.background = '#fff';

		// Change the value
		document.getElementById("dropdown-arrow").name = 2;

	} else {
		// Means to close the button
		// Change the icon
		document.getElementById("dropdown-arrow").src = '../icons/arrow_right.svg';

		// Show the Menu
		document.getElementById("course-link-div").style.display = 'none';

		// Change the color of link
		//document.getElementById("courses-li").style.background = '#fff';

		// Change the value
		document.getElementById("dropdown-arrow").name = 1;

	}

	//alert(x);
}

// WHY INVEST
function whyInvest(x) {
	var detail = document.getElementById(`why-invest-detail${x}`);
	detail.style.display = 'block';


	//hidding contents
	var heading = document.getElementById(`outside-heading${x}`);
	heading.style.display = 'none';

	// Changing the background of Why invest
	var why_invest = document.getElementById(`why-invest${x}`);
	//why_invest.style.backgroundColor = 'var(--brand-green)';   //rgb(16, 224, 224, 0.8)
	why_invest.style.backgroundSize = 'cover';
	why_invest.style.backgroundRepeat = 'no-repeat';

	if (x == 1) {
		why_invest.style.backgroundImage = "url('static/images/i-01.png')";
	}
	else if (x == 2) {
		why_invest.style.backgroundImage = "url('static/images/i-02.png')";
	}
	else if (x == 3) {
		why_invest.style.backgroundImage = "url('static/images/i-03.png')";
	}
	else if (x == 4) {
		why_invest.style.backgroundImage = "url('static/images/i-04.png')";
	}
}

// Close Why Invest
function closeWhyInvest() {
	for (var x = 1; x <= 4; x++) {
		var heading = document.getElementById(`outside-heading${x}`);
		heading.style.display = 'block';

		//close every why invest div
		var detail = document.getElementById(`why-invest-detail${x}`);
		detail.style.display = 'none';

		// Changing the background of Why invest
		var why_invest = document.getElementById(`why-invest${x}`);
		why_invest.style.backgroundColor = '#FFFFF4';
		why_invest.style.backgroundImage = "none";

	}

}

function whyInvestC(x) {
	var why_invest = document.getElementById(`why-invest${x}`);
	var state = why_invest.title;

	if (state == 1) {
		//show why-ivest-div
		var detail = document.getElementById(`why-invest-detail${x}`);
		detail.style.display = 'block';

		//hidding contents
		var heading = document.getElementById(`outside-heading${x}`);
		heading.style.display = 'none';

		// Changing the background of Why invest
		why_invest.style.backgroundColor = 'var(--brand-green)';
		why_invest.style.backgroundSize = 'cover';
		why_invest.style.backgroundRepeat = 'no-repeat';

		if (x == 1) {
			why_invest.style.backgroundImage = "url('static/images/i-01.jpg')";
		}
		else if (x == 2) {
			why_invest.style.backgroundImage = "url('static/images/i-02.jpg')";
		}
		else if (x == 3) {
			why_invest.style.backgroundImage = "url('static/images/i-03.jpg')";
		}
		else if (x == 4) {
			why_invest.style.backgroundImage = "url('static/images/i-04.jpg')";
		}


		//alert(x);
		why_invest.title = 2;
	} else {
		//close the why invest div
		for (var y = 1; y <= 4; y++) {
			var heading = document.getElementById(`outside-heading${y}`);
			heading.style.display = 'block';

			//close every why invest div
			var detail = document.getElementById(`why-invest-detail${y}`);
			detail.style.display = 'none';

			// Changing the background of Why invest
			why_invest.style.backgroundColor = '#FFFFF4';
			why_invest.style.backgroundImage = "none";
		}


		//alert("close div");
		why_invest.title = 1;
	}

	//alert(state);

}





function viewTeamMembers() {
	document.getElementById("about_btn").style.display = "none";
	document.getElementById("team-members").style.display = "block";
	//alert(1);
}

// PROPERTY SLIDER
function nextImage() {
	if ((x < length) && (x != limit)) {
		document.getElementById("prev-image-btn").style.display = "block";
		x++;
		changeImage(property_img[x]);
		if (x == limit) {
			document.getElementById("next-image-btn").style.display = "none";
		}
	} else {
		document.getElementById("next-image-btn").style.display = "none";
	}
}

function prevImage() {
	if (x > 0) {
		document.getElementById("next-image-btn").style.display = "block";
		x--;
		changeImage(property_img[x]);
		if (x == 0) {
			document.getElementById("prev-image-btn").style.display = "none";
		}

	} else {
		document.getElementById("prev-image-btn").style.display = "none";
	}
}

function changeImage(x) {
	var link = "url('" + x + "')";
	document.getElementById("slider-image").style.backgroundImage = link;
}

function sliderStartup() {
	if (length > 0) {
		changeImage(property_img[0]);
		if (length == 1) {
			// Means only one image is available, so we hide the slider icons.
			document.getElementById("next-image-btn").style.display = "none";
			document.getElementById("prev-image-btn").style.display = "none";

		} else if (length > 1) {
			document.getElementById("prev-image-btn").style.display = "none";
		}
	}
}

// Portfolio 
function createPortfolio() {
	event.preventDefault();

	// Show the dives
	document.getElementById("portfolio-div").style.display = "block";
	document.getElementById("portfolio-div1a").style.display = "block";
	//alert(1);
}


function hideTable() {
	document.getElementById("portfolio-table").style.display = "none";
	document.getElementById("portfolio-chart3").style.display = "block";
	document.getElementById("chart-btn").style.display = "block";
	document.getElementById("drag-table2").innerHTML = "Click on the pie for details";
}

function showTable() {
	document.getElementById("portfolio-table").style.display = "block";
	document.getElementById("portfolio-chart3").style.display = "none";
	document.getElementById("chart-btn").style.display = "none";
	document.getElementById("drag-table2").innerHTML = "Drag table to see all";
}

// Referral
function copyReferralLink() {
	// Get the text field
	var copyText = document.getElementById("referral-link").innerHTML;
	copyText = copyText.trim();
	//alert(copyText);

	// Select the text field
	//copyText.select();
	//copyText.setSelectionRange(0, 99999); // For mobile devices

	// Copy the text inside the text field
	navigator.clipboard.writeText(copyText);

	var clip_icon = document.getElementById("clip-icon");
	clip_icon.style.display = "block";

	setTimeout(() => {
		clip_icon.style.display = "none";
	}, 2000);
	// Alert the copied text
	//alert("Text copied");
}


// About US Page

/*
function myalert(){
	if (document.documentElement.scrollTop > 500) {
	alert(2);
  } else {
    
  }
}*/

function howItWorks() {
	setTimeout(step1, 1000);
	//setTimeout(step3, 1000);
	//setTimeout(step4, 1000);
	//howItWorks2();
}

function step1() {
	document.getElementById("arrow1").style.visibility = "visible";
	setTimeout(step2, 1000);
	//alert(1);
}

function step2() {
	document.getElementById("arrow1").style.visibility = "hidden";
	document.getElementById("arrow2").style.visibility = "visible";
	setTimeout(step3, 1000);
}

function step3() {
	document.getElementById("arrow1").style.visibility = "hidden";
	document.getElementById("arrow2").style.visibility = "hidden";
	document.getElementById("arrow3").style.visibility = "visible";
	setTimeout(step4, 1000);
}

function step4() {
	document.getElementById("arrow1").style.visibility = "hidden";
	document.getElementById("arrow2").style.visibility = "hidden";
	document.getElementById("arrow3").style.visibility = "hidden";
	howItWorks();
}

function howItWorks2() {
	howItWorks();
}


/*	ADMIN DASHBOARD*/
function insertModule(value) {
	//Changing the span content
	var semesterSpan = document.getElementById('dropdownMenuButton2');
	semesterSpan.textContent = value;

	//Changing the form module value
	document.getElementById('moduleInput').value = value;

	// submiting the form
	document.getElementById('moduleForm').submit();
}

function addLesson() {
	event.preventDefault();

	var s = document.getElementById("myCheck1");
	var x = document.getElementById("myCheck2");
	var y = document.getElementById("myCheck3");
	var z = document.getElementById("myCheck4");

	if (s.checked) {
		//alert(s.value);
		window.location.href = 'admin-dashboard-new-lesson-text.html';

	} else if (x.checked) {
		//alert(x.value);
		window.location.href = 'admin-dashboard-new-lesson-video.html';

	} else if (y.checked) {
		//alert(y.value);
		window.location.href = 'admin-dashboard-new-lesson-file.html';

	} else if (z.checked) {
		//alert(z.value);
		window.location.href = 'admin-dashboard-new-lesson-quiz.html';
	}

}

function propertyTypeForm() {
	var property_type = document.getElementById("property-type").value;
	var location = document.getElementById("location");
	var brillianzhub = document.getElementById("Brillianzhub-properties");
	var co_owned = document.getElementById("Co-owned-properties");
	var verified_vendors = document.getElementById("Verified-Vendors-properties");

	// showing the divs based on property type
	if (property_type == 'Brillianzhub Properties') {
		location.style.display = "block";
		brillianzhub.style.display = "block";
		co_owned.style.display = "none";
		verified_vendors.style.display = "none";

	} else if (property_type == 'Co-owned Properties') {
		location.style.display = "block";
		brillianzhub.style.display = "none";
		co_owned.style.display = "block";
		verified_vendors.style.display = "none";

	} else if (property_type == 'Verified Vendors Properties') {
		location.style.display = "none";
		brillianzhub.style.display = "none";
		co_owned.style.display = "none";
		verified_vendors.style.display = "block";

	} else {
		location.style.display = "none";
		brillianzhub.style.display = "none";
		co_owned.style.display = "none";
		verified_vendors.style.display = "none";
	}

	//alert(property_type);

}