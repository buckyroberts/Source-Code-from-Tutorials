//Usually want to break up code into different files to better organize
//All movie related code can go here
//Other files can include this code
function printAvatar(){
    console.log("Avatar: PG-13");
}

function printChappie(){
    console.log("Chappie: R");
}

//What gets exported is determined by 'module.exports' variable
module.exports.avatar = printAvatar;