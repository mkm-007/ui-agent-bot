import { Component, Input } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-button',
  standalone: true,
  imports: [CommonModule],
  template: `<button type="button" [attr.data-variant]="variant">{{ label }}</button>`,
})
export class AppButton {
  @Input() label: string = 'Submit';
  @Input() variant: 'primary' | 'secondary' = 'primary';
}
