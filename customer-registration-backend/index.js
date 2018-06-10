const express = require('express');
const path = require('path');
const bodyParser = require('body-parser');
const axios = require('axios');

const app = express();

//app.use(express.static(DIST_PATH));
app.use(bodyParser.json());

app.get('/', function(req, res) {
    res.status(200);
    res.send();
    console.log("Here")
})

app.get('/auth/callback', function (req, res) {
    // this is a callback that we get from facebook
    //log.debug("/auth/callback", req.body);
    const redirect_uri = req.body.redirectUri;
    const code = req.body.code;
    console.log(redirect_uri, code)
    res.status(200);
    res.send();
});

app.get('/auth/facebook', async function (req, res) {
    // this is a callback that we get from client browser
    //log.debug("got authentication", req.body);
    console.log("GOT CALLED")
    const redirect_uri = req.body.redirectUri;
    const code = req.body.code;

    let response_access_token;
    try {
        response_access_token = await axios({
            method: "get",
            url: `https://www.facebook.com/v3.0/oauth/access_token`,
            params: {
                client_id: config.app_id,
                redirect_uri: redirect_uri,
                client_secret: config.app_secret,
                code: code
            }
        });
    } catch (err) {
        //log.error("err", err.response.data);
        throw err;
    }

    //log.debug("got response_access_token", response_access_token.data);
    const facebook_access_token = response_access_token.data.access_token;
    //const my_access_token = users.addFacebookUser(facebook_access_token);
    console.log(facebook_access_token)
    res.status(200);
    res.send({
        access_token: my_access_token
    });
});

app.listen(8070, function () {
    //log.info(`Express server listening on port 8080`);
    return;
});