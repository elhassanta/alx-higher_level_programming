#!/usr/bin/node
let myDic = require('./101-data');
let newDic = {};
Object.entries(myDic).map(e => {
  if (newDic[e[1]]){
    newDic[e[1]].push(e[0]);
  } else {
    newDic[e[1]] = [e[0]];
  }
});
