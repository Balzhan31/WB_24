function getSecondsToday() {
    let myDate = new Date();
    return myDate.getHours() * 3600 + myDate.getMinutes() * 60 + myDate.getSeconds();
  }

  alert(getSecondsToday());