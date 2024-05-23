import { ComponentFixture, TestBed } from '@angular/core/testing';

import { VetlistComponent } from './vetlist.component';

describe('VetlistComponent', () => {
  let component: VetlistComponent;
  let fixture: ComponentFixture<VetlistComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [VetlistComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(VetlistComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
