import React, { useState } from "react";
import './Roulette.css';
import apple from './assets/apple.png';
import banana from "./assets/banana.png";
import grape from "./assets/grape.png";
import pumpkin from "./assets/pumpkin.png";
import meat from "./assets/meat.png";
import carrot from "./assets/carrot.png";
import steak from "./assets/steak.png";
import chicken from "./assets/chicken.png";
import fish from "./assets/fish.png";
import { useNavigate } from "react-router-dom";
import './bubble-right.css';

const options = ['Vegetable', 'Seafood', 'Fruit', 'Meat'];
const imageOptions = [banana, grape, pumpkin, meat, carrot, steak, chicken, fish, apple];

const Roulette = () => {
  const [selections, setSelections] = useState(Array(3).fill('Vegetable'));
  const [images, setImages] = useState(Array(3).fill(apple));
  const [clicked, setClicked] = useState(false);
  const [names, setNames] = useState(Array(3).fill('Brussel Sprouts'));
  const [costs, setCosts] = useState(Array(3).fill(0));
  const [links, setLinks] = useState(Array(3).fill('/'))
  const navigate = useNavigate();

  const handleSpinAll = () => {
    setClicked(true);
    for (let index = 0; index < images.length; index++) {
      handleReroll(index);
    }
  };

  const handleReroll = (index) => {
    let counter = 0;
    const interval = setInterval(() => {
      setImages((currentImages) => currentImages.map((img, i) => {
        if (i === index) {
          return imageOptions[Math.floor(Math.random() * imageOptions.length)];
        }
        return img;
      }));
  
      counter++;
      if (counter > 10) {
        clearInterval(interval);
        showIngredient(index, selections[index]);
      }
    }, 100);
  };

  const setSelection = (value, index) => {
    setSelections(choices => 
      choices.map((item, i) => i === index ? value : item)
    );
  }

  const recipe = () => {
    localStorage.setItem('ingredients', JSON.stringify(names));
    navigate('/recipe');
  }

  const showIngredient = async (index, category) => {
    const response = await fetch(`/get-ingredient?category=${category}`);
    const responseData = await response.json();
    setImages((currentImages) => currentImages.map((img, i) => {
      if (i === index) {
        return responseData.image;
      }
      return img;
    }));
    setNames((currentNames) => currentNames.map((name, i) => {
      if (i === index) {
        return responseData.name;
      }
      return name;
    }));
    setCosts((currentCosts) => currentCosts.map((cost, i) => {
      if (i === index) {
        return responseData.cost;
      }
      return cost;
    }));
    setLinks((currentLinks) => currentLinks.map((link, i) => {
      if (i === index) {
        return responseData.link;
      }
      return link;
    }));
  }

  return (
    <div className="page">
      <div className="container">
        <h1 className="title">Test Your Luck</h1>
        <div className="box-row">
          {images.map((imageSrc, index) => (
            <div key={index} className="box-container">
              <div className="box">
                {clicked &&<p className="ing-name">{names[index]}</p>}
                {!clicked &&<img src={imageSrc} alt={`Slot ${index}`} />}
                {clicked &&<a href={links[index]} target="_blank" rel="noopener noreferrer">
                  <img src={imageSrc} alt={`Slot ${index}`} />
                </a>}
                {clicked &&<p className="ing-cost">${costs[index]}</p>}
              </div>
              {clicked && <button className="rerollButton btn-22 rerollType" onClick={() => handleReroll(index)}><span >Reroll</span></button>}
              <div class="select-wrapper">
                <select class="drop-down" value={selections[index]} onChange={e => setSelection(e.target.value, index)}>
                  {options.map(option => (
                    <option key={option} value={option}>{option}</option>
                  ))}
                </select>
            </div>
            </div>
          ))}
        </div>
        <button onClick={handleSpinAll} className="spinButton btn-22 spinType"><span>Spin All</span></button>
        {clicked &&<button onClick={recipe} className="btn-22 recipeButton recipeType"><span>Find Recipe</span></button>}
      </div>
    </div>
  );
};

export default Roulette;