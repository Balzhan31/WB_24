function makeUser() {
    return {
        name: "Jake",
        ref() {
            return this;
        }
    };
}

let user = makeUser();

alert(user.ref().name); 
// Jake