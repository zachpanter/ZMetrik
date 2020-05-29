import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { RauminhaltComponent } from './rauminhalt.component';

describe('RauminhaltComponent', () => {
  let component: RauminhaltComponent;
  let fixture: ComponentFixture<RauminhaltComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ RauminhaltComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(RauminhaltComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
