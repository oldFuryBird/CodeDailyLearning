function timeFormat(time, formater = 'Y-m-d H:i:s') {
  if (!(time instanceof Date)) {
    throw new Error('`time` must be an Date object')
  }

  const o = {
    'Y': time.getFullYear(),
    'm': time.getMonth() + 1,
    'd': time.getDate(),
    'H': time.getHours(),
    'i': time.getMinutes(),
    's': time.getSeconds()
  }
  for (let k in o) {
	   if (new RegExp('(' + k + ')').test(formater)) {
     formater = formater.replace(RegExp.$1, function (key) {
       k !== 'Y' && o[k].toString().length === 1 && (o[k] = '0' + o[k])
       return o[k]
     })
   }
  }

  return formater
}
/*
	var now = new Date()
	console.log(now,'Y-m-d H:i')
	console.log(now,'Y-m')
	console.log(now,'Y')
	console.log(now)	
*/
	var now = new Date("2017-12-9")
	console.log(timeFormat(now,'Y-m-d H:i'))
	console.log(timeFormat(now,'Y-m'))
	console.log(timeFormat(now,'Y'))
	console.log(timeFormat(now))	
