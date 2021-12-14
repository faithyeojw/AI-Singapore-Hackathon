"""
Node template for creating custom nodes.
"""

from gtts import gTTS
from playsound import playsound
from typing import Any, Dict
from peekingduck.pipeline.nodes.node import AbstractNode

class Node(AbstractNode):
    """This is a template class of how to write a node for PeekingDuck.
    Args:
        config (:obj:`Dict[str, Any]` | :obj:`None`): Node configuration.
    """
    def __init__(self, config: Dict[str, Any] = None, **kwargs: Any) -> None:
        super().__init__(config, node_path=__name__, **kwargs)
        self.mytext = 'Watch the road !'
        self.language = 'en'
        self.say = gTTS(text=self.mytext, lang=self.language, slow=False)
        self.say.save("watchout.mp3")
        # initialize/load any configs and models here
        # configs can be called by self.<config_name> e.g. self.filepath
        self.logger.info(f"model loaded with configs: "+str(config))

    def run(self, inputs: Dict[str, Any]) -> Dict[str, Any]:  # type: ignore
        """This node does ___.
        Args:
            inputs (dict): Dictionary with keys "__", "__".
        Returns:
            outputs (dict): Dictionary with keys "__".
        """
        if len(inputs["keypoint_scores"]) > 0:

            self.logger.info("Nose Detected with " + str(inputs["keypoint_scores"][0][0] * 100) + " confidence")
            self.logger.info("Left Eye Detected with " + str(inputs["keypoint_scores"][0][1] * 100) + " confidence")
            self.logger.info("Right Eye Detected with " + str(inputs["keypoint_scores"][0][2] * 100) + " confidence")

            if inputs["keypoint_scores"][0][0]>0.5 or inputs["keypoint_scores"][0][1]>0.5 or inputs["keypoint_scores"][0][2] > 0.5:
                playsound('watchout.mp3')
        return {'direction': 'Left'}

        # result = do_something(inputs["in1"], inputs["in2"])
        # outputs = {"out1": result}
        # return outputs
