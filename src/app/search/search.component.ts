import { Component } from '@angular/core';
import { FormGroup, FormControl , Validators} from '@angular/forms';
// import { HttpClient } from '@angular/common/http';
// import { Observable } from 'rxjs';
@Component({
  selector: 'app-search',
  templateUrl: './search.component.html',
  styleUrl: './search.component.css'
  
})
export class SearchComponent {
  private baseUrl = 'http://127.0.0.1:5000/api/types/';  
  types: any[] = [];
  typeNames: any[] = [];

  selectedValue: string;
  options = [
    // { value: 'household-pets', label: 'Household pets' },
    // { value: 'reptile', label: 'Reptiles' },
    // // { value: 'ruminants', label: 'Ruminants (Cows & Horses)' },
    // { value: 'farm', label: 'Farm'},
    // { value: 'aquatic', label: 'Aquatic' },
    // { value: 'rodents', label: 'Rodents' },
    // { value: 'exotic', label: 'Exotic' },
    // { value: 'zoo', label: 'Zoo' }
    
  ];
  
  
  initSelect() {
    this.options = this.typeNames.map(item => ({ value: item, label: item }));
    // console.log(this.options);
    // console.log("dbiidihdiqwjhdiqwuhdiuwdhiqdwud");
  }

  getType() {
    fetch(this.baseUrl)
      .then(response => {
        if (!response.ok) {
          throw new Error('Network response was not ok ' + response.statusText);
        }
        return response.json();
      })
      .then(json => {
        if (Array.isArray(json)) {
          this.types = json;
        } else if (json.types && Array.isArray(json.types)) {
          // If the array is nested inside an object with a key, e.g., json.types
          this.types = json.types;
        } else {
          throw new Error('Fetched data does not contain an array');
        }
        // Log the fetched array of objects
        // console.log('Fetched types:', this.types); 

        this.typeNames = this.types.map(item => item.type);
        // console.log('Type names:', this.typeNames); // Log the array of type names

        // if (this.types.length > 0) {
        //   console.log('First type:', this.types[0].type);
        // }
        this.initSelect();
      })
      .catch(err => console.error('Fetch error:', err));
  }


  
  constructor() { 
    this.getType();
   }
  title = 'Pawsibilities';
  searchForm = new FormGroup({
    name: new FormControl(""),
    city: new FormControl(""),
    type: new FormControl("")
  });
  callbackAddpet = function () {
    console.log("callback adapt train called");
  }

  
  addpet = function () {
    const petUrl = 'http://127.0.0.1:5000/api/pets/';
    
    const jsonObject = JSON.stringify({
      // breed : document.querySelector('.js-add-breed').value,
      // species: document.querySelector('.js-add-species').value,
      // name: document.querySelector('.js-add-age').value,
      // sterilized : document.querySelector('.js-add-sterilized').value,
      // microchip : document.querySelector('.js-add-microchip').value,
      // gender : document.querySelector('.js-add-gender').value,
      // year_of_birth : document.querySelector('.js-add-year_of_birth').value
      breed : "German Shepherd",
      species: "Dog",
      name: "Shakira",
      sterilized : 1,
      microchip : 9090303,
      gender : 'F',
      year_of_birth : 2012
    })

    handleData(petUrl, 'POST', jsonObject);
    handleData(petUrl);
  }

  

  onSubmit(event) {
    event.preventDefault()
    const formData = this.searchForm.value;
    formData.type = this.selectedValue;
    console.log(formData);
    this.addpet();
  }
  
  
  onRadioChange(value: string) {
    this.selectedValue = value;
  }
}


const handleData = function (url, method = 'GET', body = null) {
  fetch(url, {
    method: method,
    body: body,
    headers: {'Content-Type': 'application/json', 'User-Agent': 'insomnia/8.6.0'},
  })
    .then(function (response) {
      if (!response.ok) {
        console.warn(`>> Problem with fetch(). Statuscode: ${response.status}`);
      } else {
        console.info('>>Response from server came back');
        return response.json();
      }
    })
    .then(function (jsonObject) {
      if (jsonObject) {
        console.info('>> JSONobject is made');
        // return jsonObject;
      }
    })
    .catch(function (error) {
      console.warn(`>>fault with parsing: ${error}`);
    });
};