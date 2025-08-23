import 'package:flet/flet.dart';

import 'flet_secure_storage.dart';

CreateControlFactory createControl = (CreateControlArgs args) {
  switch (args.control.type) {
    case "flet_secure_storage":
      return FletSecureStorageControl(
        parent: args.parent,
        control: args.control,
      );
    default:
      return null;
  }
};

void ensureInitialized() {
  // nothing to initialize
}
