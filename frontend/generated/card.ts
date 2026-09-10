import { Component, Input } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-card',
  standalone: true,
  imports: [CommonModule],
  template: `<article><h2>{{ title }}</h2><p>{{ body }}</p></article>`,
})
export class AppCard {
  @Input() title: string = 'Card';
  @Input() body: string = '';
}
