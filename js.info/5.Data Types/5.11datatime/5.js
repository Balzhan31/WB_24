function getLastDayOfMonth(year, month) {
    let date = new Date(year, month + 1, 0);
    return date.getDate();
  }

  alert(getLastDayOfMonth(2012, 3)); // 30
  alert(getLastDayOfMonth(2012, 6)); // 31
  alert(getLastDayOfMonth(2013, 1)); // 28