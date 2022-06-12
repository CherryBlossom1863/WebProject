function switchTab(evt, tabName) {
  let elem = document.getElementsById("navigation_bar");
  let tablinks =  document.querySelectorAll('.a');
  for (i = 0; i < tablinks.length; i++) {
      tablinks[i].className = tablinks[i].className.replace("active", "");
  }
  document.getElementById(tabName).style.display = "block";
  evt.currentTarget.className += " active";
}
