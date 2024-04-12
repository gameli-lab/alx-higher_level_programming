#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12,
  incre:function() {
	  this.value++;
  }
};
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);

