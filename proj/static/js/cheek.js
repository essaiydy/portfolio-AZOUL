function Cheek(
  email,
  password,
  msgemail = "Incorrect email or account doesn't exist !"
) {
  let emailholder = document.getElementById("email");
  let passwordholder = document.getElementById("password");

  if (email === "false") {
    origHol = emailholder.placeholder;
    backgroundEmail = emailholder.style.background;
    origOutli = emailholder.style.outline;
    emailholder.placeholder = msgemail;
    emailholder.style.background = "pink";
    emailholder.style.outline = "2px solid white";
    setTimeout(function () {
      emailholder.placeholder = origHol;
      emailholder.style.background = backgroundEmail;
      emailholder.style.outline = origOutli;
    }, 2500);
    return;
  }

  if (password === "false") {
    origPlaceHol = passwordholder.placeholder;
    origColor = passwordholder.style.background;
    origOutli = passwordholder.style.outline;
    passwordholder.placeholder = "incorrect password";
    passwordholder.style.background = "pink";
    passwordholder.style.outline = "2px solid white";
    setTimeout(function () {
      passwordholder.placeholder = origPlaceHol;
      passwordholder.style.background = origColor;
      passwordholder.style.outline = origOutli;
    }, 2500);
  }
}
