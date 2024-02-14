function formatDate(date) {
    let diffrnc = new Date() - date;
    if (diffrnc < 1000) return "right now";

    let sec = Math.floor(diffrnc / 1000); 
    if (sec < 60) return sec + " sec. ago";

    let min = Math.floor(diffrnc / 60000); 
    if (min < 60) return min + " min. ago";

    let myDate = date;
    myDate = [
      "0" + myDate.getDate(),
      "0" + (myDate.getMonth() + 1),
      "" + myDate.getFullYear(),
      "0" + myDate.getHours(),
      "0" + myDate.getMinutes(),
    ].map((component) => component.slice(-2));

    return myDate.slice(0, 3).join(".") + " " + myDate.slice(3).join(":");
  }

  alert(formatDate(new Date(new Date() - 1))); // "right now"
  alert(formatDate(new Date(new Date() - 30 * 1000))); // "30 sec. ago"
  alert(formatDate(new Date(new Date() - 5 * 60 * 1000))); // "5 min. ago"
  alert(formatDate(new Date(new Date() - 86400 * 1000)));