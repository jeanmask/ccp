(function () {
  function OffersCtrl($scope, Restangular, lodash) {
    function toQuerySlider(that, field) {
        var values = {};

        if ('value' in that) {
          values[field] = that.value;
        }
        else {
          if(that.min != that.options.minLimit) {
            values['min_' + field] = that.min;
          }
          if(that.max != that.options.maxLimit) {
            values['max_' + field] = that.max;
          }
        }

        return values;
    }

    function getSellers() {
      Restangular
        .all('sellers')
        .getList()
        .then(function (sellers) {
          $scope.sellers = sellers.plain();
        });
    }

    function getOffers() {
      // Default options
      var parsedFilters = {'ordering': 'exchanged_price'};

      lodash($scope.filters)
        .forEach(function (item) {
          var q = item.toQuery();
          if (q) {
            parsedFilters = lodash.extend(parsedFilters, q);
          }
        });

      Restangular
        .all('offers')
        .getList(parsedFilters)
        .then(function (offers) {
          $scope.offers = offers.plain();
        });
    }

    function changeCurrency() {
      $scope.$broadcast('rzSliderForceRender');
      getOffers();
    }

    $scope.filters = {
      exchangeCurrency: {
        value: 'USD',
        toQuery: function() {
          if (this.value) {
            return {'exchange_currency': this.value};
          }
          return false;
        }
      },
      seller: {
        value: null,
        toQuery: function () {
          if (this.value) {
            return {'seller': this.value};
          }
          return false;
        }
      },
      cpuCores: {
        min: 1,
        max: 18,
        toQuery: function () {
          return toQuerySlider(this, 'cpu_cores')
        },
        options: {
          floor: 1,
          minLimit: 1,
          maxLimit: 18,
          showTicks: true,
          showTicksValues: true,
          translate: function(value) {
            return value + (value == 18 ? '+' : '');
          }
        },
      },
      memorySize: {
        min: 0,
        max: 50,
        toQuery: function () {
          return lodash(toQuerySlider(this, 'memory_size'))
            .mapValues(function(value) {
              return value * 1024 * 1024 * 1024;
            })
            .value();
        },
        options: {
          minLimit: 0,
          maxLimit: 50,
          minRange: 2,
          translate: function(value) {
            return value + ' GB' + (value == 50 ? '+' : '');
          },
        },
      },
      diskSize: {
        min: 0,
        max: 1024,
        toQuery: function () {
          return lodash(toQuerySlider(this, 'disk_size'))
            .mapValues(function(value) {
              return value * 1024 * 1024 * 1024;
            })
            .value();
        },
        options: {
          minRange: 10,
          minLimit: 0,
          maxLimit: 1024,
          step: 2,
          translate: function(value) {
            if (value == 1024) {
              return '1 TB+';
            }
            return value + ' GB';
          },
        },
      },
      price: {
        min: 0,
        max: 500,
        toQuery: function () {
          return toQuerySlider(this, 'price');
        },
        options: {
          id: 'priceSlider',
          maxLimit: 500,
          minLimit: 0,
          minRange: 5,
          step: 5,
          translate: function(value) {
            return $scope.filters.exchangeCurrency.value + ' ' + value + (value == 500 ? '+' : '');
          },
        },
      },
    };

    $scope.offers = [];
    $scope.getOffers = getOffers;

    $scope.sellers = [];
    $scope.getSellers = getSellers;

    $scope.changeCurrency = changeCurrency;

    getSellers();
    getOffers();
  }

  angular.module('app.controllers', [])
    .controller('offersCtrl', ['$scope', 'Restangular', 'lodash', OffersCtrl]);
})();