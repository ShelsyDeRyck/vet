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
  private baseUrl = 'http://127.0.0.1:5000/api/types';  
  types: any[] = [];

  // constructor(private http: HttpClient) { 
  //   console.log(this.getType());
  // }

  // getTypes(): Observable<Type[]> {
  //   return this.http.get<Type[]>(this.baseUrl);
  // }

  getType() {
    // return this.http.get(this.baseUrl);
    fetch(this.baseUrl)
    .then(response => response.json())
    .then(json => {
        this.types = json;
        console.log('Types:', this.types);
      })
    .catch(err => console.error(err));
  }

  

  // searchRecipe() {
  //   fetch(this.url)
  //     .then(response => response.json())
  //     .then(json => {
  //         this.recipes = json;
  //         this.search = this.recipes.filter(recipes => recipes.title.includes(this.mySearch));
  //       if (this.search) {
  //         console.log('Recipes:', this.search);
  //       } else {
  //         console.log(`No recipes found for ${this.search}`);
  //       }
  //     })
  //     .catch(err => console.error(err));
  // }
  constructor() { this.getType(); }
  title = 'Pawsibilities';
  searchForm = new FormGroup({
    name: new FormControl(""),
    city: new FormControl(""),
    type: new FormControl("")
  });

  onSubmit(event) {
    event.preventDefault()
    const formData = this.searchForm.value;
    formData.type = this.selectedValue;
    console.log(formData);
  }

  selectedValue: string;
  options = [
    { value: 'household-pets', label: 'Household pets' },
    { value: 'reptile', label: 'Reptiles' },
    // { value: 'ruminants', label: 'Ruminants (Cows & Horses)' },
    { value: 'farm', label: 'Farm'},
    { value: 'aquatic', label: 'Aquatic' },
    { value: 'rodents', label: 'Rodents' },
    { value: 'exotic', label: 'Exotic' },
    { value: 'zoo', label: 'Zoo' }
  ];
  

  onRadioChange(value: string) {
    this.selectedValue = value;
  }
}
