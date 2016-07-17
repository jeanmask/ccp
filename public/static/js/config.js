(function () {
  function RestangularConfig(RestangularProvider) {
      RestangularProvider.setBaseUrl('/api');
  }

  angular
  .module('app')
  .config([
    'RestangularProvider',
    RestangularConfig
  ]);
})();