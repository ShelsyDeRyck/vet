import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

// import { SearchComponent } from './search/search.component';
import { VetlistComponent } from './vetlist/vetlist.component';

export const routes: Routes = [
  {  
    path: '',
    redirectTo: 'home',
    pathMatch: 'full', 
  },
  {
    path: 'list',
    component: VetlistComponent
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
