import { Component } from '@angular/core';
import { FormGroup, FormControl , Validators} from '@angular/forms';
@Component({
  selector: 'app-search',
  templateUrl: './search.component.html',
  styleUrl: './search.component.css'
  
})
export class SearchComponent {

  constructor() { }
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
