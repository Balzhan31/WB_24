function getDateAgo(date, pastDays) {
    let date2 = new Date(date);
    date2.setDate(date.getDate() - pastDays);
    return date2.getDate();
  }

  let date = new Date(2015, 0, 2);
  alert(getDateAgo(date, 1)); // 1, (1 Jan 2015)
  alert(getDateAgo(date, 2)); // 31, (31 Dec 2014)
  alert(getDateAgo(date, 365)); // 2, (2 Jan 2014)