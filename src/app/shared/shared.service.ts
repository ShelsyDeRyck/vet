import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class SharedService {
  private formData: FormData = new FormData();

  constructor() { }

  setFormData(data: FormData): void {
    this.formData = data;
  }

   getFormData(): FormData {
    return this.formData;
  }
}