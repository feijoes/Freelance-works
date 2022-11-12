const mongoose = require('mongoose');
const {User} = require('../db/coneccion');
const passport = require('passport');
const {
    genPassword,
    validPassword,
    issueJWT
} = require('../lib/passwordUtils');


const Login = (req,res,next)=>{
    User.findOne({ username: req.body.username })
    .then((user) => {

        if (!user) {
            return res.status(401).json({ success: false, msg: "could not find user" });
        }
        
        // Function defined at bottom of app.js
        const isValid = utils.validPassword(req.body.password, user.hash, user.salt);
        
        if (isValid) {

            const tokenObject = utils.issueJWT(user);

            res.status(200).json({ success: true, token: tokenObject.token, expiresIn: tokenObject.expires });

        } else {

            res.status(401).json({ success: false, msg: "you entered the wrong password" });

        }

    })
    .catch((err) => {
        next(err);
    });
    
}
const Regiter = (req,res,next)=>{
    const {
        salt,
        hash
    } = genPassword(req.body.password);

    const newUser = new User({
        username: req.body.username,
        hash : hash,
        salt: salt
    });

    newUser.save().then((user)=>{
        const jwt = issueJWT(user);

        res.json({user:user,token: jwt.token, expires: jwt.expires})
    }).catch(err => next(err))
}

module.exports={
    Login,
    Regiter
}