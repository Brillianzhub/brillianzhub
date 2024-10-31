const dropArea = document.getElementById("dropContainer1");
const dragText = dropArea.querySelector("header");
const button = dropArea.querySelector("button");
const input = dropArea.querySelector("input");
let file_name = " ";

button.onclick = ()=>{
  input.click(); //if user click on the button then the input also clicked
  file_browse();
}

input.addEventListener("change", function(){
  //getting user select file and [0] this means if user select multiple files then we'll select only the first one
  fileInput1.file = this.files;
  dropArea.classList.add("active");
  
});

//If user Drag File Over DropArea
dropContainer1.ondragover = dropContainer1.ondragenter = function(evt) {
  evt.preventDefault();
		dropArea.classList.add("active");
		dragText.textContent = "Release to Upload File";
};

//If user leave dragged File from DropArea
dropContainer1.ondragleave = function(evt) {
  	evt.preventDefault();
		dropArea.classList.remove("active");
		dragText.textContent = "Drag & Drop to Upload File";
};

//If user Drag File Over DropArea
dropContainer1.ondrop = function(evt) {
  // pretty simple -- but not for IE :(
  fileInput1.files = evt.dataTransfer.files;
  const number_files = evt.dataTransfer.files.length;
  const filesh = evt.dataTransfer.files;
  //alert(evt.dataTransfer.files[0].name);

  for (let i = 0; i < number_files; i++) {
  	let y =  evt.dataTransfer.files[i].name;
  	
  	if(i == 0){
		file_name = file_name.concat("", y);
  	}else{
  		file_name = file_name.concat(", ", y);
  	}
  	
  	//file_name += y;
  	
  }

  //alert(number_files);

  dragText.textContent = file_name;

  evt.preventDefault();
};


function upload_file(e) {
    e.preventDefault();
    fileobj = e.dataTransfer.files;
    alert(fileobj);
    
}

function file_browse() {
  document.getElementById('fileInput1').onchange = function() {
   	fileobj = document.getElementById('fileInput1').files;
    //alert(fileobj.length);

  for (let i = 0; i < fileobj.length; i++) {
  	let y =  fileobj[i].name;
  	
  	if(i == 0){
		file_name = file_name.concat("", y);
  	}else{
  		file_name = file_name.concat(", ", y);
  	}
  	
  }


  dragText.textContent = file_name;
      
  };
}

const dropArea2 = document.getElementById("dropContainer2");
const dragText2 = dropArea2.querySelector("header");
const button2 = dropArea2.querySelector("button");
const input2 = dropArea2.querySelector("input");
let file_name2 = " ";

button2.onclick = ()=>{
  input2.click(); //if user click on the button then the input also clicked
  file_browse2();
}

input2.addEventListener("change", function(){
  //getting user select file and [0] this means if user select multiple files then we'll select only the first one
  fileInput2.file = this.files;
  dropArea2.classList.add("active");
  
});

//If user Drag File Over DropArea
dropContainer2.ondragover = dropContainer2.ondragenter = function(evt) {
  evt.preventDefault();
		dropArea.classList.add("active");
		dragText.textContent = "Release to Upload File";
};

//If user leave dragged File from DropArea
dropContainer2.ondragleave = function(evt) {
  	evt.preventDefault();
		dropArea.classList.remove("active");
		dragText.textContent = "Drag & Drop to Upload File";
};

//If user Drag File Over DropArea
dropContainer2.ondrop = function(evt) {
  // pretty simple -- but not for IE :(
  fileInput2.files = evt.dataTransfer.files;
  const number_files = evt.dataTransfer.files.length;
  const filesh = evt.dataTransfer.files;
  //alert(evt.dataTransfer.files[0].name);

  for (let i = 0; i < number_files; i++) {
  	let y =  evt.dataTransfer.files[i].name;
  	
  	if(i == 0){
		file_name2 = file_name2.concat("", y);
  	}else{
  		file_name2 = file_name2.concat(", ", y);
  	}
  	
  	//file_name += y;
  	
  }

  //alert(number_files);

  dragText2.textContent = file_name2;

  evt.preventDefault();
};


function upload_file2(e) {
    e.preventDefault();
    fileobj = e.dataTransfer.files;
    alert(fileobj);
    
}

function file_browse2() {
  document.getElementById('fileInput2').onchange = function() {
   	fileobj = document.getElementById('fileInput2').files;
    //alert(fileobj.length);

  for (let i = 0; i < fileobj.length; i++) {
  	let y =  fileobj[i].name;
  	
  	if(i == 0){
		file_name2 = file_name2.concat("", y);
  	}else{
  		file_name2 = file_name2.concat(", ", y);
  	}
  	
  }


  dragText2.textContent = file_name2;
      
  };
}

const dropArea3 = document.getElementById("dropContainer3");
const dragText3 = dropArea3.querySelector("header");
const button3 = dropArea3.querySelector("button");
const input3 = dropArea3.querySelector("input");
let file_name3 = " ";

button3.onclick = ()=>{
  input3.click(); //if user click on the button then the input also clicked
  file_browse3();
}

input3.addEventListener("change", function(){
  //getting user select file and [0] this means if user select multiple files then we'll select only the first one
  fileInput3.file = this.files;
  dropArea3.classList.add("active");
  
});

//If user Drag File Over DropArea
dropContainer3.ondragover = dropContainer3.ondragenter = function(evt) {
  evt.preventDefault();
		dropArea.classList.add("active");
		dragText.textContent = "Release to Upload File";
};

//If user leave dragged File from DropArea
dropContainer3.ondragleave = function(evt) {
  	evt.preventDefault();
		dropArea.classList.remove("active");
		dragText.textContent = "Drag & Drop to Upload File";
};

//If user Drag File Over DropArea
dropContainer3.ondrop = function(evt) {
  // pretty simple -- but not for IE :(
  fileInput3.files = evt.dataTransfer.files;
  const number_files = evt.dataTransfer.files.length;
  const filesh = evt.dataTransfer.files;
  //alert(evt.dataTransfer.files[0].name);

  for (let i = 0; i < number_files; i++) {
  	let y =  evt.dataTransfer.files[i].name;
  	
  	if(i == 0){
		file_name3 = file_name3.concat("", y);
  	}else{
  		file_name3 = file_name3.concat(", ", y);
  	}
  	
  	//file_name += y;
  	
  }

  //alert(number_files);

  dragText3.textContent = file_name3;

  evt.preventDefault();
};


function upload_file3(e) {
    e.preventDefault();
    fileobj = e.dataTransfer.files;
    alert(fileobj);
    
}

function file_browse3() {
  document.getElementById('fileInput3').onchange = function() {
   	fileobj = document.getElementById('fileInput3').files;
    //alert(fileobj.length);

  for (let i = 0; i < fileobj.length; i++) {
  	let y =  fileobj[i].name;
  	
  	if(i == 0){
		file_name3 = file_name3.concat("", y);
  	}else{
  		file_name3 = file_name3.concat(", ", y);
  	}
  	
  }


  dragText3.textContent = file_name3;
      
  };
}

const dropArea4 = document.getElementById("dropContainer4");
const dragText4 = dropArea4.querySelector("header");
const button4 = dropArea4.querySelector("button");
const input4 = dropArea4.querySelector("input");
let file_name4 = " ";

button4.onclick = ()=>{
  input4.click(); //if user click on the button then the input also clicked
  file_browse4();
}

input4.addEventListener("change", function(){
  //getting user select file and [0] this means if user select multiple files then we'll select only the first one
  fileInput4.file = this.files;
  dropArea4.classList.add("active");
  
});

//If user Drag File Over DropArea
dropContainer4.ondragover = dropContainer4.ondragenter = function(evt) {
  evt.preventDefault();
		dropArea.classList.add("active");
		dragText.textContent = "Release to Upload File";
};

//If user leave dragged File from DropArea
dropContainer4.ondragleave = function(evt) {
  	evt.preventDefault();
		dropArea.classList.remove("active");
		dragText.textContent = "Drag & Drop to Upload File";
};

//If user Drag File Over DropArea
dropContainer4.ondrop = function(evt) {
  // pretty simple -- but not for IE :(
  fileInput4.files = evt.dataTransfer.files;
  const number_files = evt.dataTransfer.files.length;
  const filesh = evt.dataTransfer.files;
  //alert(evt.dataTransfer.files[0].name);

  for (let i = 0; i < number_files; i++) {
  	let y =  evt.dataTransfer.files[i].name;
  	
  	if(i == 0){
		file_name4 = file_name4.concat("", y);
  	}else{
  		file_name4 = file_name4.concat(", ", y);
  	}
  	
  	//file_name += y;
  	
  }

  //alert(number_files);

  dragText4.textContent = file_name4;

  evt.preventDefault();
};


function upload_file4(e) {
    e.preventDefault();
    fileobj = e.dataTransfer.files;
    alert(fileobj);
    
}

function file_browse4() {
  document.getElementById('fileInput4').onchange = function() {
   	fileobj = document.getElementById('fileInput4').files;
    //alert(fileobj.length);

  for (let i = 0; i < fileobj.length; i++) {
  	let y =  fileobj[i].name;
  	
  	if(i == 0){
		file_name4 = file_name4.concat("", y);
  	}else{
  		file_name4 = file_name4.concat(", ", y);
  	}
  	
  }


  dragText4.textContent = file_name4;
      
  };
}

const dropArea5 = document.getElementById("dropContainer5");
const dragText5 = dropArea5.querySelector("header");
const button5 = dropArea5.querySelector("button");
const input5 = dropArea5.querySelector("input");
let file_name5 = " ";

button5.onclick = ()=>{
  input5.click(); //if user click on the button then the input also clicked
  file_browse5();
}

input5.addEventListener("change", function(){
  //getting user select file and [0] this means if user select multiple files then we'll select only the first one
  fileInput5.file = this.files;
  dropArea5.classList.add("active");
  
});

//If user Drag File Over DropArea
dropContainer5.ondragover = dropContainer5.ondragenter = function(evt) {
  evt.preventDefault();
		dropArea.classList.add("active");
		dragText.textContent = "Release to Upload File";
};

//If user leave dragged File from DropArea
dropContainer5.ondragleave = function(evt) {
  	evt.preventDefault();
		dropArea.classList.remove("active");
		dragText.textContent = "Drag & Drop to Upload File";
};

//If user Drag File Over DropArea
dropContainer5.ondrop = function(evt) {
  // pretty simple -- but not for IE :(
  fileInput5.files = evt.dataTransfer.files;
  const number_files = evt.dataTransfer.files.length;
  const filesh = evt.dataTransfer.files;
  //alert(evt.dataTransfer.files[0].name);

  for (let i = 0; i < number_files; i++) {
  	let y =  evt.dataTransfer.files[i].name;
  	
  	if(i == 0){
		file_name5 = file_name5.concat("", y);
  	}else{
  		file_name5 = file_name5.concat(", ", y);
  	}
  	
  	//file_name += y;
  	
  }

  //alert(number_files);

  dragText5.textContent = file_name5;

  evt.preventDefault();
};


function upload_file5(e) {
    e.preventDefault();
    fileobj = e.dataTransfer.files;
    alert(fileobj);
    
}

function file_browse5() {
  document.getElementById('fileInput5').onchange = function() {
   	fileobj = document.getElementById('fileInput5').files;
    //alert(fileobj.length);

  for (let i = 0; i < fileobj.length; i++) {
  	let y =  fileobj[i].name;
  	
  	if(i == 0){
		file_name5 = file_name5.concat("", y);
  	}else{
  		file_name5 = file_name5.concat(", ", y);
  	}
  	
  }


  dragText5.textContent = file_name5;
      
  };
}

const dropArea6 = document.getElementById("dropContainer6");
const dragText6 = dropArea6.querySelector("header");
const button6 = dropArea6.querySelector("button");
const input6 = dropArea6.querySelector("input");
let file_name6 = " ";

button6.onclick = ()=>{
  input6.click(); //if user click on the button then the input also clicked
  file_browse6();
}

input6.addEventListener("change", function(){
  //getting user select file and [0] this means if user select multiple files then we'll select only the first one
  fileInput6.file = this.files;
  dropArea6.classList.add("active");
  
});

//If user Drag File Over DropArea
dropContainer6.ondragover = dropContainer6.ondragenter = function(evt) {
  evt.preventDefault();
		dropArea.classList.add("active");
		dragText.textContent = "Release to Upload File";
};

//If user leave dragged File from DropArea
dropContainer6.ondragleave = function(evt) {
  	evt.preventDefault();
		dropArea.classList.remove("active");
		dragText.textContent = "Drag & Drop to Upload File";
};

//If user Drag File Over DropArea
dropContainer6.ondrop = function(evt) {
  // pretty simple -- but not for IE :(
  fileInput6.files = evt.dataTransfer.files;
  const number_files = evt.dataTransfer.files.length;
  const filesh = evt.dataTransfer.files;
  //alert(evt.dataTransfer.files[0].name);

  for (let i = 0; i < number_files; i++) {
  	let y =  evt.dataTransfer.files[i].name;
  	
  	if(i == 0){
		file_name6 = file_name6.concat("", y);
  	}else{
  		file_name6 = file_name6.concat(", ", y);
  	}
  	
  	//file_name += y;
  	
  }

  //alert(number_files);

  dragText6.textContent = file_name6;

  evt.preventDefault();
};


function upload_file6(e) {
    e.preventDefault();
    fileobj = e.dataTransfer.files;
    alert(fileobj);
    
}

function file_browse6() {
  document.getElementById('fileInput6').onchange = function() {
   	fileobj = document.getElementById('fileInput6').files;
    //alert(fileobj.length);

  for (let i = 0; i < fileobj.length; i++) {
  	let y =  fileobj[i].name;
  	
  	if(i == 0){
		file_name6 = file_name6.concat("", y);
  	}else{
  		file_name6 = file_name6.concat(", ", y);
  	}
  	
  }


  dragText6.textContent = file_name6;
      
  };
}

const dropArea7 = document.getElementById("dropContainer7");
const dragText7 = dropArea7.querySelector("header");
const button7 = dropArea7.querySelector("button");
const input7 = dropArea7.querySelector("input");
let file_name7 = " ";

button7.onclick = ()=>{
  input7.click(); //if user click on the button then the input also clicked
  file_browse7();
}

input7.addEventListener("change", function(){
  //getting user select file and [0] this means if user select multiple files then we'll select only the first one
  fileInput7.file = this.files;
  dropArea7.classList.add("active");
  
});

//If user Drag File Over DropArea
dropContainer7.ondragover = dropContainer7.ondragenter = function(evt) {
  evt.preventDefault();
		dropArea.classList.add("active");
		dragText.textContent = "Release to Upload File";
};

//If user leave dragged File from DropArea
dropContainer7.ondragleave = function(evt) {
  	evt.preventDefault();
		dropArea.classList.remove("active");
		dragText.textContent = "Drag & Drop to Upload File";
};

//If user Drag File Over DropArea
dropContainer7.ondrop = function(evt) {
  // pretty simple -- but not for IE :(
  fileInput7.files = evt.dataTransfer.files;
  const number_files = evt.dataTransfer.files.length;
  const filesh = evt.dataTransfer.files;
  //alert(evt.dataTransfer.files[0].name);

  for (let i = 0; i < number_files; i++) {
  	let y =  evt.dataTransfer.files[i].name;
  	
  	if(i == 0){
		file_name7 = file_name7.concat("", y);
  	}else{
  		file_name7 = file_name7.concat(", ", y);
  	}
  	
  	//file_name += y;
  	
  }

  //alert(number_files);

  dragText7.textContent = file_name7;

  evt.preventDefault();
};


function upload_file7(e) {
    e.preventDefault();
    fileobj = e.dataTransfer.files;
    alert(fileobj);
    
}

function file_browse7() {
  document.getElementById('fileInput7').onchange = function() {
   	fileobj = document.getElementById('fileInput7').files;
    //alert(fileobj.length);

  for (let i = 0; i < fileobj.length; i++) {
  	let y =  fileobj[i].name;
  	
  	if(i == 0){
		file_name7 = file_name7.concat("", y);
  	}else{
  		file_name7 = file_name7.concat(", ", y);
  	}
  	
  }


  dragText7.textContent = file_name7;
      
  };
}

const dropArea8 = document.getElementById("dropContainer8");
const dragText8 = dropArea8.querySelector("header");
const button8 = dropArea8.querySelector("button");
const input8 = dropArea8.querySelector("input");
let file_name8 = " ";

button8.onclick = ()=>{
  input8.click(); //if user click on the button then the input also clicked
  file_browse8();
}

input8.addEventListener("change", function(){
  //getting user select file and [0] this means if user select multiple files then we'll select only the first one
  fileInput8.file = this.files;
  dropArea8.classList.add("active");
  
});

//If user Drag File Over DropArea
dropContainer8.ondragover = dropContainer8.ondragenter = function(evt) {
  evt.preventDefault();
		dropArea.classList.add("active");
		dragText.textContent = "Release to Upload File";
};

//If user leave dragged File from DropArea
dropContainer8.ondragleave = function(evt) {
  	evt.preventDefault();
		dropArea.classList.remove("active");
		dragText.textContent = "Drag & Drop to Upload File";
};

//If user Drag File Over DropArea
dropContainer8.ondrop = function(evt) {
  // pretty simple -- but not for IE :(
  fileInput8.files = evt.dataTransfer.files;
  const number_files = evt.dataTransfer.files.length;
  const filesh = evt.dataTransfer.files;
  //alert(evt.dataTransfer.files[0].name);

  for (let i = 0; i < number_files; i++) {
  	let y =  evt.dataTransfer.files[i].name;
  	
  	if(i == 0){
		file_name8 = file_name8.concat("", y);
  	}else{
  		file_name8 = file_name8.concat(", ", y);
  	}
  	
  	//file_name += y;
  	
  }

  //alert(number_files);

  dragText8.textContent = file_name8;

  evt.preventDefault();
};


function upload_file8(e) {
    e.preventDefault();
    fileobj = e.dataTransfer.files;
    alert(fileobj);
    
}

function file_browse8() {
  document.getElementById('fileInput8').onchange = function() {
   	fileobj = document.getElementById('fileInput8').files;
    //alert(fileobj.length);

  for (let i = 0; i < fileobj.length; i++) {
  	let y =  fileobj[i].name;
  	
  	if(i == 0){
		file_name8 = file_name8.concat("", y);
  	}else{
  		file_name8 = file_name8.concat(", ", y);
  	}
  	
  }


  dragText8.textContent = file_name8;
      
  };
}

const dropArea9 = document.getElementById("dropContainer9");
const dragText9 = dropArea9.querySelector("header");
const button9 = dropArea9.querySelector("button");
const input9 = dropArea9.querySelector("input");
let file_name9 = " ";

button9.onclick = ()=>{
  input9.click(); //if user click on the button then the input also clicked
  file_browse9();
}

input9.addEventListener("change", function(){
  //getting user select file and [0] this means if user select multiple files then we'll select only the first one
  fileInput9.file = this.files;
  dropArea9.classList.add("active");
  
});

//If user Drag File Over DropArea
dropContainer9.ondragover = dropContainer9.ondragenter = function(evt) {
  evt.preventDefault();
		dropArea.classList.add("active");
		dragText.textContent = "Release to Upload File";
};

//If user leave dragged File from DropArea
dropContainer9.ondragleave = function(evt) {
  	evt.preventDefault();
		dropArea.classList.remove("active");
		dragText.textContent = "Drag & Drop to Upload File";
};

//If user Drag File Over DropArea
dropContainer9.ondrop = function(evt) {
  // pretty simple -- but not for IE :(
  fileInput9.files = evt.dataTransfer.files;
  const number_files = evt.dataTransfer.files.length;
  const filesh = evt.dataTransfer.files;
  //alert(evt.dataTransfer.files[0].name);

  for (let i = 0; i < number_files; i++) {
  	let y =  evt.dataTransfer.files[i].name;
  	
  	if(i == 0){
		file_name9 = file_name9.concat("", y);
  	}else{
  		file_name9 = file_name9.concat(", ", y);
  	}
  	
  	//file_name += y;
  	
  }

  //alert(number_files);

  dragText9.textContent = file_name9;

  evt.preventDefault();
};


function upload_file9(e) {
    e.preventDefault();
    fileobj = e.dataTransfer.files;
    alert(fileobj);
    
}

function file_browse9() {
  document.getElementById('fileInput9').onchange = function() {
   	fileobj = document.getElementById('fileInput9').files;
    //alert(fileobj.length);

  for (let i = 0; i < fileobj.length; i++) {
  	let y =  fileobj[i].name;
  	
  	if(i == 0){
		file_name9 = file_name9.concat("", y);
  	}else{
  		file_name9 = file_name9.concat(", ", y);
  	}
  	
  }


  dragText9.textContent = file_name9;
      
  };
}

const dropArea10 = document.getElementById("dropContainer10");
const dragText10 = dropArea10.querySelector("header");
const button10 = dropArea10.querySelector("button");
const input10 = dropArea10.querySelector("input");
let file_name10 = " ";

button10.onclick = ()=>{
  input10.click(); //if user click on the button then the input also clicked
  file_browse10();
}

input10.addEventListener("change", function(){
  //getting user select file and [0] this means if user select multiple files then we'll select only the first one
  fileInput10.file = this.files;
  dropArea10.classList.add("active");
  
});

//If user Drag File Over DropArea
dropContainer10.ondragover = dropContainer10.ondragenter = function(evt) {
  evt.preventDefault();
		dropArea.classList.add("active");
		dragText.textContent = "Release to Upload File";
};

//If user leave dragged File from DropArea
dropContainer10.ondragleave = function(evt) {
  	evt.preventDefault();
		dropArea.classList.remove("active");
		dragText.textContent = "Drag & Drop to Upload File";
};

//If user Drag File Over DropArea
dropContainer10.ondrop = function(evt) {
  // pretty simple -- but not for IE :(
  fileInput10.files = evt.dataTransfer.files;
  const number_files = evt.dataTransfer.files.length;
  const filesh = evt.dataTransfer.files;
  //alert(evt.dataTransfer.files[0].name);

  for (let i = 0; i < number_files; i++) {
  	let y =  evt.dataTransfer.files[i].name;
  	
  	if(i == 0){
		file_name10 = file_name10.concat("", y);
  	}else{
  		file_name10 = file_name10.concat(", ", y);
  	}
  	
  	//file_name += y;
  	
  }

  //alert(number_files);

  dragText10.textContent = file_name10;

  evt.preventDefault();
};


function upload_file10(e) {
    e.preventDefault();
    fileobj = e.dataTransfer.files;
    alert(fileobj);
    
}

function file_browse10() {
  document.getElementById('fileInput10').onchange = function() {
   	fileobj = document.getElementById('fileInput10').files;
    //alert(fileobj.length);

  for (let i = 0; i < fileobj.length; i++) {
  	let y =  fileobj[i].name;
  	
  	if(i == 0){
		file_name10 = file_name10.concat("", y);
  	}else{
  		file_name10 = file_name10.concat(", ", y);
  	}
  	
  }


  dragText10.textContent = file_name10;
      
  };
}



















	