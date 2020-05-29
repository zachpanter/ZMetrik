import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { NahrungComponent } from './nahrung.component';

describe('NahrungComponent', () => {
  let component: NahrungComponent;
  let fixture: ComponentFixture<NahrungComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ NahrungComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(NahrungComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
