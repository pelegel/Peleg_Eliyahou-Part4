/*pull the pathname of the active page from window location.
put an "active" class to the active page by creating an array of the nav's links and comparing
each path name to the currently active page*/
const activePage = window.location.pathname;
const navLinks = document.querySelectorAll('nav a').forEach(link => {
  if(link.href.includes(`${activePage}`)){
    link.classList.add('active');
  }
});



