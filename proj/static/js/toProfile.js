function toProfile(id) {
  const redirect = document.getElementById(id);
  redirect.addEventListener("click", () => {
    window.location.href = "http://localhost:5000/profiles/id";
  });
}
