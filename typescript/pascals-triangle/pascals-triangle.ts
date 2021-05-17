export default class Triangle {
  private height: number;
  private numbers: number[][] = [];

  constructor(height: number) {
    this.height = height;

    for (let i = 0; i < height; i++) {
      this.numbers.push([1]);
      for (let j = 0; j < i; j++) {
        if(j >= i - 1) {
          this.numbers[i].push(1);
        } else {
          this.numbers[i].push(this.numbers[i - 1][j] + this.numbers[i - 1][j + 1]);
        }
      }
    }
  }

  public get rows(): number[][] {
    return this.numbers;
  }

  public get lastRow(): number[] {
    return this.numbers[this.numbers.length - 1];
  }
}