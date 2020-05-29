import { AppPage } from './app.po';
import { browser, logging } from 'protractor';

describe('workspace-project App', () => {
  let page: AppPage;

  beforeEach(() => {
    page = new AppPage();
  });

  // it('should display welcome message', () => {
  //   page.navigateTo();
  //   expect(page.getTitleText()).toEqual('zmetrik-ng app is running!');
  // });

  it('should allow entry of new food', () => {
      // TODO: Implement
  });

  it('should allow entry of new weightlifting sets', () => {
    // TODO: Implement
  });

  it('should allow entry of new morphometric measurements', () => {
    // TODO: Implement
});

  afterEach(async () => {
    // Assert that there are no errors emitted from the browser
    const logs = await browser.manage().logs().get(logging.Type.BROWSER);
    expect(logs).not.toContain(jasmine.objectContaining({
      level: logging.Level.SEVERE,
    } as logging.Entry));
  });
});
