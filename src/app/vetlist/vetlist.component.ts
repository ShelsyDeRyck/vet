import { Component } from '@angular/core';
import { SharedService } from '../shared/shared.service';

@Component({
  selector: 'app-vetlist',
  templateUrl: './vetlist.component.html',
  styleUrl: './vetlist.component.css'
})
export class VetlistComponent {
  receivedFormData: FormData;

  constructor(private sharedService: SharedService) { }

  ngOnInit(): void {
    // Retrieve the FormData instance from the shared service
    this.receivedFormData = this.sharedService.getFormData();

    // Log the FormData entries for debugging purposes
    this.logFormDataEntries();
  }

  logFormDataEntries(): void {
    this.receivedFormData.forEach((value, key) => {
      console.log(`${key}: ${value}`);
    });
  }

  // Example method to convert FormData to a JSON object
  getFormDataAsJson(): any {
    const jsonObject: any = {};
    this.receivedFormData.forEach((value, key) => {
      jsonObject[key] = value;
    });
    return jsonObject;
  }
}