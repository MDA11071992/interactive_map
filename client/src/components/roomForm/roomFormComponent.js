angular
  .module('app')
  .component('roomFormComponent', {
    templateUrl: '/src/components/roomForm/roomFormView.html',
    bindings: {
        room: '<'
    },
    controller: roomFormComponentController
  });

function roomFormComponentController($scope) {

  var vm = this;
  vm.$onInit = onInit;
  vm.removeRoom = removeRoom;

  function onInit() {
    vm.room.coordinate = vm.room.coordinate || {};

  }

  function removeRoom() {
    $scope.$emit('removeRoomListener', vm.room);
  }

}