import React from "react";
import PropTypes from "prop-types";

Food.propTypes = {
    name: PropTypes.string.isRequired,
    picture: PropTypes.string.isRequired,
    rating: PropTypes.number
}

function Food({fav}){
    return <h1>I like {fav}</h1>
}


export default Food;