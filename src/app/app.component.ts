import { Component } from '@angular/core';
import { FormGroup, FormControl , Validators} from '@angular/forms';
// import { HttpClient } from '@angular/common/http';


@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
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
    { value: 'household-pets', label: 'household pets' },
    { value: 'reptile', label: 'Reptiles' },
    { value: 'ruminants', label: 'Ruminants (Cows & Horses)' },
    { value: 'aquatic', label: 'Aquatic' },
    { value: 'rodents', label: 'Rodents' },
    { value: 'exotic', label: 'Exotic' },
    { value: 'zoo', label: 'Zoo' }
  ];
  

  onRadioChange(value: string) {
    this.selectedValue = value;
  }
}
