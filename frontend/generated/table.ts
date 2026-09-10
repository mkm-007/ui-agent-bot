import { Component, Input } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-data-table',
  standalone: true,
  imports: [CommonModule],
  template: `<table><caption>{{ caption }}</caption><thead><tr><th scope="col" *ngFor="let column of columns">{{ column }}</th></tr></thead><tbody><tr *ngFor="let row of rows"><td *ngFor="let column of columns">{{ row[column] }}</td></tr></tbody></table>`,
})
export class AppDataTable {
  @Input() caption: string = 'Data';
  @Input() columns: string[] = [];
  @Input() rows: Record<string, string | number>[] = [];
}
