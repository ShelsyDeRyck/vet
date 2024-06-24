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
        this.typeNames = this.types.map(item => item.type);
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
  

  
  addpet = function () {
    const petUrl = 'http://127.0.0.1:5000/api/pets/';
    
    const jsonObject = JSON.stringify({
      breed : "German Shepherd",
      species: "Dog",
      name: "Shakira",
      sterilized : 1,
      microchip : 9090303,
      gender : 'F',
      year_of_birth : 2012
    })

    // handleData(petUrl, 'POST', jsonObject);
    handleData(petUrl);
  }

  

  onSubmit(event) {
    event.preventDefault();

    // Extracting form data from the reactive form
    const formData = this.searchForm.value;
    formData.type = this.selectedValue; 
    console.log(formData);

    // let search = callbackFunction(formData);
    // console.log(search);
    callbackFunction(formData).then((data) => {
      console.log(data);
    })
    // console.log(this.addpet());
  }
  
  
  onRadioChange(value: string) {
    this.selectedValue = value;
  }
}

async function callbackFunction(formData) {
  try {
    const urlWithParams = `http://127.0.0.1:5000/api/vets/search/?location=${encodeURIComponent(formData.city)}&name=${encodeURIComponent(formData.name)}&type=${encodeURIComponent(formData.type)}`;
    let result = await handleData(urlWithParams, 'GET', JSON.stringify(formData));
    // console.log(result);
    // console.log(typeof result);
    return result;
  } catch (error) {
    console.error('Error:', error);
  }
}


const handleData = function (url, method = 'GET', body: any = null) {
  const options: RequestInit = {
    method: method,
    headers: {
      'Content-Type': 'application/json',
      'User-Agent': 'insomnia/8.6.0'
    },
  };

  // Conditionally add the body property
  if (body && (method === 'POST' || method === 'PUT' || method === 'PATCH')) {
    options.body = body;
  }

  return fetch(url, options)
    .then(response => {
      if (!response.ok) {
        console.warn(`>> Problem with fetch(). Status code: ${response.status}`);
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      console.info('>> Response from server came back');
      return response.json();
    })
    .then(jsonObject => {
      console.info('>> JSON object is made');
      return jsonObject;  // Ensure the JSON object is returned
    })
    .catch(error => {
      console.warn(`>> Fault with parsing: ${error}`);
      throw error;  // Ensure the error is propagated
    });
};