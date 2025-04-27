from abc import ABC, abstractmethod

class RenderableInterface(ABC):
    @abstractmethod
    def update_entity_view(self) -> None :
        """_summary_
        """
        pass

    @abstractmethod
    def display_entity_view(self, screen) -> None :
        """_summary_

        Args:
            screen (_type_): _description_
        """
        pass