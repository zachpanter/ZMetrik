import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { MorphometriksComponent } from './morphometriks.component';

describe('MorphometriksComponent', () => {
  let component: MorphometriksComponent;
  let fixture: ComponentFixture<MorphometriksComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ MorphometriksComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(MorphometriksComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
